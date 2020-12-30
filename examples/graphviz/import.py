"""
This example shows the interals of certain Python modules when they are being
imported.
"""
from pycallgraph import Config, PyCallGraph
from pycallgraph.output import GraphvizOutput


def main():
    import_list = (
        "pickle",
        "html.parser",
        "requests",
        # TODO: import-requests.png is not generated as the other two libraries.
    )
    graphviz = GraphvizOutput()
    config = Config(include_stdlib=True)

    for module in import_list:
        graphviz.output_file = f"import-{module}.png"
        with PyCallGraph(output=graphviz, config=config):
            __import__(module)


if __name__ == "__main__":
    main()
