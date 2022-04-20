#!/usr/bin/env python
import os
import sys
import nbformat
import azure.storage.blob
import base64



def replace_images(nb, credentail):
    cc = azure.storage.blob.ContainerClient(
        "https://ai4edatasetspublicassets.blob.core.windows.net",
        "assets",
        credential=credential,
    )
    content_settings = azure.storage.blob.ContentSettings(conent_type="image/png")

    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            outputs = cell["outputs"]
            for output in outputs:
                if output["output_type"] == "display_data" and list(output["data"])[0] == "image/png":
                    print("replace", cell["execution_count"])
                    b64png = output["data"].pop("image/png").encode()
                    output["metadata"].pop("needs_background", None)
                    output["output_type"] = "display_data"
                    png = base64.b64decode(b64png)
                    url = "https://ai4edatasetspublicassets.blob.core.windows.net/assets"
                    name = f"notebook-output/customizable-rtc-sentine1.ipynb/{cell['execution_count']}.png"
                    cc.upload_blob(name, png, content_settings=content_settings, overwrite=True)
                    output["data"]["text/html"] = f'<img src="{url}/{name}"/>'


if __name__ == "__main__":
    path = sys.argv[1]
    credential = os.environ["PLANETARY_COMPUTER_EXAMPLES_SAS"]
    nb = nbformat.read(path, as_version=4)
    replace_images(nb, credentail=credential)
    nbformat.write(nb, path)
