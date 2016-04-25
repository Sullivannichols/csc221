#!/usr/bin/env python3

print("\n")

user = int(input("Enter a leap year to check\n:"))
leap_year = user % 4

if user % 400 == 0:
    print("%s is a leap year" % user)
elif user % 100 == 0:
    print("%s is not a leap year" % user)
elif leap_year == 0:
    print("%s is a leap year" % user)
elif leap_year != 0:
    print("%s is not a leap year" % user)
else:
    print("try another year")
