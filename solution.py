# put two numbers no space between!
print("Enter two numbers to see every number between them.. Please add space between numbers")
user_input = input("Enter two numbers here: ")

# as you put two numbers they are in string, you may want to use .split() -> now they are two string in an array.
numbers = user_input.split()
print(numbers)

numbers_without_five = []
num1 = int(numbers[0])
num2 = int(numbers[1])

for i in range(num1, num2 + 1):
    if "5" not in str(i):
        numbers_without_five.append(i)

print(numbers_without_five)