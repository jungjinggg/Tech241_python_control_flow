# Control Flow

Control flow allows blocks of code or statements to be executed based on conditions.

### Conditional Statements
conditional statements are used to perform decision-making.
```python
age = int(input("How old are you?: "))

# conditions
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
```

```python
temp = int(input("What is the temperature?: "))

# conditions
if temp >= 25:
    print("Let's make BBQ")
elif temp >= 15:
    print("Let's go for a walk")
elif temp >= 10:
    print("Let's go hiking")
elif temp >= 5:
    print("Let's go camping")
else:
    print("Let's just stay in and watch a movie")
```
The block of code will get executed based on the user input.
### For Loops
a for loop is used to iterate through a sequence of data
```python
list_data = [1, 2, 3, 4, 5]

# a loop that iterate through list_data
for num in list_data:
    print(num * 2)
```
```python
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}
# looping through dictionaries
for item in dict_data.values():
    for key, j in item.items():
        print(f'{key}: {j}')

# a loop that only return money values
for items in dict_data.values():
    print(items["money"])
```
**Nested loop**

A loop within a loop
```python
embedded_list = [[1, 2, 3], [4, 5, 6]]

# looping through a nested loop
for data in embedded_list:
    # print(data)
    for num in data:
        print(num)
```
### While Loops

```python
x = 0

while x < 10:
    print(f"it's working -> {x}")
    # increment term
    x += 1

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1
```
```python
user_prompt = True

while user_prompt:
    age = input("What is your age?: ")
    if age.isdigit() and int(age) < 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age}")
```
