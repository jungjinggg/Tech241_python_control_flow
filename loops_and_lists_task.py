# Make a loop with a range that says hello 10 times
#
# for i, num in enumerate(range(10), 1):
#     print(i, "Hello!")
#
# # Create another loop with a range that asks for names and appends to a list called list_names
# list_names = []
#
# for i in range(10):
#     user_name = input("Please enter a name: ").capitalize()
#     list_names.append(user_name)
# print(list_names)
#
# # Make a loop that iterates over each name in list_name and format's it into lowercase in a new list called list_names_lower
# list_names_lower = []
#
# for name in list_names:
#     name = name.lower()
#     list_names_lower.append(name)
# print(list_names_lower)

# Make a list of numbers, iterate over the list of values to find if they are even. Print the even numbers.
# num_list = [1, 11, 12, 22, 34, 45, 53, 56, 78, 79, 101, 102, 155, 176]
#
# for num in num_list:
#     if num % 2 == 0:
#         print(num)


total_sum = 0
for i, num in enumerate(range(100)):
    total_sum += num
    print(i, total_sum)

sum_even = 0
sum_odd = 0

for num in range(100):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of even numbers")
print(sum_even)
print("Sum of odd numbers")
print(sum_odd)

