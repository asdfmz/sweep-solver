import pytest
from sympy import Matrix, Rational
from utils.sympy_codec import matrix_to_string_list, string_list_to_matrix


def test_matrix_to_string_list_and_back():
    original = Matrix([[1, 2], [-3/4, "x"], [0, 5]])
    str_list = matrix_to_string_list(original)
    reconstructed = string_list_to_matrix(str_list)
    assert reconstructed == original


def test_string_list_format():
    matrix = Matrix([[1, -2], [Rational("7/2"), 4]])
    str_list = matrix_to_string_list(matrix)
    assert str_list == ["1 -2", "7/2 4"]
    assert string_list_to_matrix(str_list) == matrix


def test_empty_matrix():
    matrix = Matrix([])
    str_list = matrix_to_string_list(matrix)
    assert str_list == []
    reconstructed = string_list_to_matrix(str_list)
    assert reconstructed == matrix
