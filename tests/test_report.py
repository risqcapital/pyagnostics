from rich.console import Console
from rich.text import Text

from pyagnostics.report import LabeledSourceBlock


def test_labeled_source_block_preserves_whitespace() -> None:
    console = Console(width=80, record=True)
    block = LabeledSourceBlock(Text("a  b\nc"))

    console.print(block)
    output = console.export_text()

    assert "a  b" in output
