#!/usr/local/bin/python3
import re
import nbformat
import rich
import sys


xpr = re.compile("^#", re.MULTILINE)
single_header = re.compile("^# ", re.MULTILINE)
double_header = re.compile("^## ", re.MULTILINE)


def main():
    errors = False
    for filename in sys.argv[1:]:
        doc = nbformat.read(filename, nbformat.current_nbformat)
        header_cells = [
            x
            for x in doc.cells
            if x["cell_type"] == "markdown" and xpr.search(x["source"])
        ]
        bad_cells = [x for x in header_cells if single_header.search(x["source"])]
        toplevel = [x for x in header_cells if double_header.search(x["source"])]

        if bad_cells:
            for cell in bad_cells:
                source = cell["source"]
                try:
                    end = source.index("\n")
                except ValueError:
                    end = None
                slice_ = slice(None, end)
                rich.print(
                    f"[red]{filename}[/red] - H1 header -",
                    source[slice_],
                )
            errors = True
        if len(toplevel) == 0:
            rich.print(f"[red]{filename}[/red] - No H2")
            errors = True
        elif len(toplevel) > 1:
            rich.print(f"[red]{filename}[/red] - {len(toplevel)} H2s")
            errors = True

    sys.exit(int(errors))


if __name__ == "__main__":
    main()
