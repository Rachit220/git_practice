from app.models.calculator import Calculator
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(4, 2) == 8

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
