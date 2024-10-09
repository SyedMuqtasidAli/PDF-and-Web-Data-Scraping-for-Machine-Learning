import math

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply a by b and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result. Handles division by zero."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


