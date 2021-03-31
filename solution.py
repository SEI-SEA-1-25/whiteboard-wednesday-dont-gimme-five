
def print_numbers():
    num1, num2 = input('Please give me two any numbers').split()
    num1 = int(num1)
    num2 = int(num2)

    for num in range(num1, num2 + 1):
        if not "5" in str(num):
        print(num)

print_numbers()

