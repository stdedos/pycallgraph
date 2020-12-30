"""
This example is trying to make a large graph. You'll need some internet access
for this to work.
"""

from pycallgraph import Config, PyCallGraph
from pycallgraph.output import GraphvizOutput


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = "large.png"
    config = Config(include_stdlib=True)

    with PyCallGraph(output=graphviz, config=config):
        from xml.dom.minidom import parseString

        import requests

        parseString(requests.get("https://w3.org/").content)


if __name__ == "__main__":
    main()
