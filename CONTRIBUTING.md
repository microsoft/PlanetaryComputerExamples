# Planetary Computer Examples

This repository contains Jupyter Notebooks that serve as examples of using the [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) data, APIs and Hub.

## Getting Started

Follow the [setup instructions in README.md](README.md#getting-started).
Microsoft employees must use
<https://packagefeedproxy.microsoft.io/pypi/simple>. Other contributors can use
<https://pypi.org/simple>. Set `UV_DEFAULT_INDEX` to your required index before
installing packages or updating requirements. Keep any feed credentials outside
the repository.

The minimum supported Python version is 3.12. The installer creates a local
`.venv` using Python 3.12, matching CI. uv downloads
Python if needed. Common dependencies are declared in
[pyproject.toml](pyproject.toml). [requirements.txt](requirements.txt) records exact
versions of direct and transitive dependencies. It is generated with
uv and contains no index URLs, so it works with either package index.

Start JupyterLab with:

```sh
uv run jupyter lab
```

Open the URL printed in the terminal. In VS Code, select `.venv/bin/python` as the
Python interpreter and notebook kernel. On Windows, use `.venv/Scripts/python.exe`
and run `scripts/install` from a Bash shell.

The shared environment covers common Python notebook dependencies. Specialized
examples may need extra packages, credentials, or remote services. R notebooks
need a separate R environment.

To regenerate requirements after editing `pyproject.toml`, run:

```sh
uv pip compile pyproject.toml --extra dev --universal --python-version 3.12 \
    --output-file requirements.txt
./scripts/install
```

The installer only installs requirements; it does not regenerate them. Add
`--upgrade-package package` to the compile command to update a specific package,
or `--upgrade` to update all packages. Commit both dependency files. Use `uv pip`
commands for this environment; automatic project syncing is disabled so `uv run`
cannot replace the compiled requirements with a different resolution.

### Linting

Notebooks are linted and formatted using
[nbQA](https://nbqa.readthedocs.io/en/latest/) with
[Ruff](https://docs.astral.sh/ruff/). The
[pre-commit configuration](.pre-commit-config.yaml) pins both tools.

```sh
uv run pre-commit install
./scripts/test --lint
```

The test script runs every pre-commit hook over all tracked files, regardless of
the current directory. Formatters may modify files; review those changes and
rerun the command until it passes.

Ruff formats at 88 columns and checks line lengths at 94 columns. Imports may
appear after other notebook code. The R quickstart is excluded from both Ruff
hooks. Notebook header checks remain unchanged.

Hook environments install packages with pip. Microsoft employees must set
`PIP_INDEX_URL=https://packagefeedproxy.microsoft.io/pypi/simple` before running
pre-commit. Other contributors can use `PIP_INDEX_URL=https://pypi.org/simple`.

Notebooks should start with an H2-level header (`## <title>`) and should have no H1-level headers.


### Integration with Data Catalog site

The notebooks from this repository are consumed by the Planetary Computer Data Catalog (the website): <https://planetarycomputer.microsoft.com>, but the code for the website is now managed privately by Microsoft.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit <https://cla.opensource.microsoft.com>.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
