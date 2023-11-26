def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    if 1<= day_of_week <= 7:
        return days[day_of_week - 1]
    else:
        return None

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed!")