"""
If statement

Write up your control flow notes in markdown first

Make a new version of the movie rating program. This version should:

Ask the user for their age
Program should tell them what rated movies they can watch (so if 13 they can watch U, PG and 12 rated movies)
Do not let the user enter an incorrect value (ages over 117 and ages under 1)
Digits only for user input, strings should prompt the user to enter a valid input. (optional)
Use if, elif and else to achieve this.
"""

# User input
try:
    age = int(input("How old are you?: "))

    if 1 < age > 118:
        print("Please enter a number between 1 - 117")
    elif age >= 18:
        print("You can watch all movies!")
    elif age >= 15:
        print("Sorry you can't watch 18 rated movies, but you can watch U, PG, 12 and 15 rated movies")
    elif age >= 12:
        print("Sorry you can't watch 18 or 15 rated movies, but you can watch U, PG, and 12 rated movies")
    elif age >= 8:
        print("Sorry you can't watch 18, 15 or 12 rated movies, but you can watch U and PG rated movies")
    elif age >= 1:
        print("You can only watch U rated movies")

except ValueError:
    print("Please enter your age as a digit")