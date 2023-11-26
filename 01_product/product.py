def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a*b

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed!")