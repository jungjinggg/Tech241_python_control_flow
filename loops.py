# for loops and while loop

# 2 types of loops in python

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

# for num in list_data:
#     print(num * 2)

# nested loops
# for data in embedded_list:
#     # print(data)
#     for num in data:
#         print(num)

# looping through dictionaries
for item in dict_data.values():
    for key, j in item.items():
        print(f'{key}: {j}')

# a loop that only return money values
for items in dict_data.values():
    print(items["money"])

# loops and if statements
for num in list_data:
    if num == 3:
        print("You have found three!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")