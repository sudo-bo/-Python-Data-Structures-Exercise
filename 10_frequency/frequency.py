def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed!")