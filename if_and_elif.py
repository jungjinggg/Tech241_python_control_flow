# Control flow

# like giving python a recipe or an order to do things

# Conditional statements

# User input
age_str = input("How old are you?: ").lower()
age = int(age_str)

if age >= 18:
    print("You can watch all movies!")
elif age >= 15:
    print("Sorry you can't watch 18 rated movies, but you can watch other movies")
elif age >= 12:
    print("Sorry you can't watch 18 or 15 rated movies, but you can watch other movies")
elif age >= 8:
    print("Sorry you can't watch 18, 15 or 12 rated movies, but you can watch other movies")
else:
    print("You can only watch u rated movies")

# There are no case or switch statements in python

