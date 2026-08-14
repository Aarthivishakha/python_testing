import pytest

from combined_analysis import evaluate_order


def test_member_discount():
    assert evaluate_order(150, True) == pytest.approx(127.5)


def test_non_member():
    assert evaluate_order(50, False) == 50
