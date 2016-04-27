Leap

Write a program that will take a year and report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

Implement a function is_leap_year(year) that takes one parameter, year (an integer), and returns True if the year is a leap year and False otherwise.

A complete set of unit tests for this function shall be included, using both the unittest and doctest modules.

