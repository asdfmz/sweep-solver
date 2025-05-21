import pytest
from sympy import Matrix, Rational
from utils.sympy_codec import (
    matrix_to_json_serializable,
    matrix_from_json_serializable
)

def test_matrix_to_json_and_back():
    original = Matrix([[1, 2], [-3/4, "x"], [0, 5]])
    json_data = matrix_to_json_serializable(original)
    reconstructed = matrix_from_json_serializable(json_data)
    assert reconstructed == original

def test_json_format():
    matrix = Matrix([[1, -2], [Rational("7/2"), 4]])
    json_data = matrix_to_json_serializable(matrix)
    assert json_data == [["1", "-2"], ["7/2", "4"]]
    assert matrix_from_json_serializable(json_data) == matrix

def test_empty_matrix():
    matrix = Matrix([])
    json_data = matrix_to_json_serializable(matrix)
    assert json_data == []
    reconstructed = matrix_from_json_serializable(json_data)
    assert reconstructed == matrix
