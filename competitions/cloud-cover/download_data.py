from pathlib import Path

from cloudpathlib import AzureBlobClient, AzureBlobPath
from loguru import logger
from tqdm.contrib.concurrent import process_map
import typer

app = typer.Typer()


def download_path(path: AzureBlobPath):
    """Downloads a single cloud path."""
    try:
        if path.is_file():
            path.fspath  # downloads cloud asset to local_cache_dir
        return {"path": path, "status": "success"}
    except Exception as exc:
        logger.debug(f"Failed to download {path}. {exc}")
        return {"path": path, "status": "failed", "message": str(exc)}


@app.command()
def main(
    sas_url: str = typer.Option(
        ...,
        help="Shared Access Signature URL that allows you to access the files (starting with "
        "https://...). This can be either the SAS URL itself or a path to a file containing the "
        "SAS URL, available from the competition datasets page.",
    ),
    cloud_directory: str = typer.Option(
        "az://.",
        help="Cloudpathlib URI (`az://./<directory>`) for cloud directory to be downloaded.",
    ),
    local_directory: Path = typer.Option(
        "data",
        help="Directory on your local machine to which the files are downloaded.",
    ),
    path_list=None,
    logger=logger,
):
    """Downloads the challenge dataset to your local machine."""
    if Path(sas_url).exists():
        logger.info(f"Loading SAS URL from {sas_url}")
        sas_url = Path(sas_url).read_text().strip()

    client = AzureBlobClient(account_url=sas_url, local_cache_dir=local_directory)

    if path_list == None:
        directory = client.CloudPath(cloud_directory)
        logger.info("Retrieving path list.")
        path_list = [
            path
            for path in directory.rglob("*")
            if path._path.suffix.lower() in (".tif", ".geojson")
        ]
    else:
        path_list = [client.CloudPath(pth) for pth in path_list]
    logger.info(f"Downloading {len(path_list)} files.")
    results = process_map(download_path, path_list, total=len(path_list), chunksize=10)
    failures = [result for result in results if result["status"] == "failed"]
    if len(failures) > 0:
        logger.warning(f"{len(failures)} files failed to download.")


if __name__ == "__main__":
    app()
