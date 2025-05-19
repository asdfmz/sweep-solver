from sympy import Matrix, eye
from services.auto_solver import gaussian_elimination_steps
from models.query import OperationType


def test_gaussian_elimination_identity():
    m = Matrix([[1, 0], [0, 1]])
    steps = gaussian_elimination_steps(m)

    # 単位行列に対しては操作が一切行われないはず
    assert steps == []


def test_gaussian_elimination_simple():
    m = Matrix([[2, 4], [1, 3]])
    steps = gaussian_elimination_steps(m)

    # 実行される操作が正しい数だけ生成される（2～4程度を想定）
    assert len(steps) >= 2

    # 最終行列が行基本形（上三角）になっていることを確認
    final_matrix = steps[-1][0]
    assert final_matrix[0, 0] == 1
    assert final_matrix[1, 0] == 0

    # 各stepのQueryが適切に生成されているか
    for matrix, query in steps:
        assert query.op in {OperationType.MULTIPLY, OperationType.ADD, OperationType.SWAP}
        assert isinstance(query.factor, str)
