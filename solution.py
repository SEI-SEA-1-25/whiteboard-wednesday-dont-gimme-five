
print('Please enter two numbers')
num1 = int(input ('Number 1:'))
num2 = int(input ('Number 2:'))

try:
   

        # value = num1

        # if value < num2:
        #     value = value + 1
        #     print(value)

        for x in range(num1, num2 + 1):
            if (x%5==0):
                continue
            print(x)

        

except ValueError:
    print('Input a value')