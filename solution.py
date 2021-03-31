num1, num2 = input('Enter two numbers to give a range.\n>>').split()

num1 = int(num1)
num2 = int(num2)

for num in range(num1, num2 + 1):
    if('5' in str(num)) == False:
        print(num)

# myList = [i** for i in range(10) if i != 2]
# print(myList)


# for i i
#         print(i)
# >>> squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]