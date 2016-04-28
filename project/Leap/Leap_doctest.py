import doctest

from year import is_leap_year

def is_leap_year(year):
    """ 
    >>> year(2016)
    is a leap year
    >>> year(1994)
    is not a leap year
    >>> year(1492) 
    is a leap year
    >>> year(1983)
    is not a leap year
    >>> 

    """

    return True

if __name__ == "__main__": 
    doctest.testmod()
    test Pass
    
