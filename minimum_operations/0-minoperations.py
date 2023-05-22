#!/usr/bin/python3
""" write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0"""


def minOperations(n):
    """Function that calculates the fewest number of operations needed to
    -result in exactly n H characters in the file"""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return 0


if __name__ == "__main__":
    print(minOperations(19170307))
    print(minOperations(972))
    print(minOperations(2147483640))
    