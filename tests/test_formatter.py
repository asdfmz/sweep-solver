from models.query import Query, OperationType
from views.formatter import QueryFormatter


def test_to_latex_multiply():
    q = Query(OperationType.MULTIPLY, target=1, factor="3")
    assert QueryFormatter.to_latex(q) == "R_{2} \\to 3 R_{2}"


def test_to_latex_add():
    q = Query(OperationType.ADD, target=0, factor="-1/2", other=2)
    assert QueryFormatter.to_latex(q) == "R_{1} \\to R_{1} + -1/2 R_{3}"


def test_to_latex_swap():
    q = Query(OperationType.SWAP, target=1, factor="1", other=0)
    assert QueryFormatter.to_latex(q) == "R_{2} \\leftrightarrow R_{1}"


def test_to_human_multiply():
    q = Query(OperationType.MULTIPLY, target=0, factor="4")
    assert QueryFormatter.to_human(q) == "1行目を4倍する"


def test_to_human_add():
    q = Query(OperationType.ADD, target=1, factor="3/5", other=2)
    assert QueryFormatter.to_human(q) == "2行目に3/5倍した3行目を加える"


def test_to_human_swap():
    q = Query(OperationType.SWAP, target=2, factor="1", other=0)
    assert QueryFormatter.to_human(q) == "3行目と1行目を入れ替える"
