#!/usr/bin/env python3

def is_leap_year(year):
    ''' 
    >>> is_leap_year(2016)
    True
    >>> is_leap_year(1994)
    False
    >>> is_leap_year(2020)
    True
    '''
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False  
    elif year % 4 == 0:
        return True  
    else:
        return False



