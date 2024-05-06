#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
    n (int): The number for which factorial will be calculated.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Captures the argument passed through command line and calculates the factorial
f = factorial(int(sys.argv[1]))
print(f)
