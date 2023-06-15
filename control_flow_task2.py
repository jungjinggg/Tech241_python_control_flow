
# Write a program that asks the user for a number. If the number is odd print "The number is odd!" and if it is even print "The number is even".

user_num = int(input("Please enter a number: "))

if user_num % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

"""
FizzBuzz - Write a program that prints numbers from 1 - 100 but for multiples of 3 print "Fizz" and 
for multiples of 5 print "Buzz". 
For multiples of 3 and 5 print "FizzBuzz
"""

# for loop
for num in range(1, 100):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# while loop
num = 1
while num < 100:
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    num += 1
