# Planetary Computer Examples

This repository contains Jupyter Notebooks that serve as examples of using the [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) data, APIs and Hub.

## Getting Started

This project uses Docker to encapsulate the development environment. To set up your development
environment, have Docker installed and run:

```sh
> scripts/setup
```

If you need to rebuild the images at any point, you
can run:

```sh
> scripts/update
```

To run the jupyter notebook server, you can use:

```sh
> scripts/server
```

And browse to the URL printed in the terminal output.

From there you'll be able to run all Jupyter Notebook examples.

### Linting

Notebooks are linted using [nbqa](https://nbqa.readthedocs.io/en/latest/) with flake8 and black.
We include a [pre-commit](https://pre-commit.com/) file for running the checks.

```
> pre-commit install
```

Notebooks should start with an H2-level header (`## <title>`) and should have no H1-level headers.


### Integration with Data Catalog site

Running the `./scripts/server` script also starts a local webserver that can
source notebook files to the Planetary Computer docs site development
environment. That project is pre-configured to integrate with this server.
After running `./scripts/server` from within this project, run
`./scripts/update --devdocs` from the Planetary Computer website project and
it will treat this local instance as the source for external docs notebooks.
See that project's ETL readme for more information.

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
