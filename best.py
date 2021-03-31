class check_five():
    numbers_input = input('Enter two numbers in ascending order with a space between them\n')
    # splice inputs at the space
    # save each number to its own variable
    num1, num2 = numbers_input.split(' ')
    # convert string inputs to integers to calculate range
    int1 = int(num1)
    int2 = int(num2)
    # get inclusive range of numbers in range between int1-int2
    for i in range(int1, int2+1):
        # turn integers into strings
        # check discrete strings against the number 5
        if ("5" not in str(i)):
            # print numbers that do not contain 5
            print(i)