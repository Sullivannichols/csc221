i#!/usr/bin/env python3

from hw4_solution import (
    is_odd,
    is_even,
    is_mult_of_four,
    is_mult_of_divisor,
    both_ends,
    )

# --------------------------------------------------------------------
# Problem 1
#
# Create a function, is_odd, that takes a number and returns True if
# that number is odd.
#
# Function: is_odd
#
# parameters:
# - number
#
# returns: boolean

def test_is_odd():
    assert_is_odd(4)==False
    assert_is_odd(5)==True

# --------------------------------------------------------------------
# Problem 2
#
# Create a function, is_even, that takes a number and returns True if
# that number is even.
#
# Function: is_even
#
# parameters:
# - number
#
# returns: boolean

def test_is_even():
    assert_is-even(4)==True
    assert_is_even(5)==False

# --------------------------------------------------------------------
# Problem 3
#
# Create a function, is_mult_of_four, that takes a number and returns
# True if that number is a multiple of four.
#
# Function: is_mult_of_four
#
# parameters:
# - number
#
# returns: boolean

def test is_mult_of_four():
    assert_is_mult_of_four(20)==True
    assert_is_mult_of_four(21)==False



# --------------------------------------------------------------------
# Problem 4
#
# Create a function, is_mult_of_x, that takes a number and a divisor
# and returns True if that number is divisible by divisor
#
# Function: is_mult_of_divisor
#
# parameters:
# - number
# - divisor
#
# returns: boolean

def test_is_mult_of_divisor():
    assert_is_mult_of_divisor(0)==True
    assert_is_mult_of_divisor(1)==False


# --------------------------------------------------------------------
# Problem 5
#
# Given a string s, return a string made of the first 2 and the last 2
# chars of the original string, so 'spring' yields 'spng'. However, if
# the string length is less than 2, return instead the empty string.
#
# Function: both_ends
#
# parameters:
# - s
#
# returns: string
def test_both_ends():
    imports=[
        ('spring', 'spong'),
        ('a', ''),
        ("",""),
        ('ab','abab'),
        ('abc', 'abbc'),
        ('abcd', 'abcd'),

    for iarg, output in inputs:
        assert both_ends(arg)==output





