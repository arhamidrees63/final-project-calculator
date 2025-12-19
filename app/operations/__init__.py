# app/operations.py

"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, division, and exponentiation of two numbers. These functions are
foundational for building more complex applications, such as calculators or financial tools.

Functions:
- add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]
- subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]
- multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]
- divide(a: Union[int, float], b: Union[int, float]) -> float
- exponentiation(a: Union[int, float], b: Union[int, float]) -> float

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform arithmetic operations based on user input.
"""

from typing import Union  # Import Union for type hinting multiple possible types

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers and return the result.
    """
    result = a + b
    return result


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first and return the result.
    """
    result = a - b
    return result


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers and return the product.
    """
    result = a * b
    return result


def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second and return the quotient.

    Raises:
    - ValueError: If b is zero, as division by zero is undefined.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")

    result = a / b
    return result


# ✅ NEW FEATURE: Exponentiation (power)
def exponentiation(a: Number, b: Number) -> float:
    """
    Raise a to the power of b and return the result as float.

    Example:
    >>> exponentiation(2, 3)
    8.0
    """
    return float(a) ** float(b)
