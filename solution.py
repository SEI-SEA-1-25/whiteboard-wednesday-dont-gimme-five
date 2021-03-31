class check_five():
    numbers_input = input('Enter two numbers in ascending order with a space between them\n')
    # print(f'{numbers_input}')
    # splice inputs at the space
    split_nums = numbers_input.split(' ')
    # print(f'{split_nums}')

    # save each number to its own variable
    num1, num2 = split_nums
    # print(f'{num1}')
    # print(f'{num2}')
    # convert string inputs to integers
    int1 = int(num1)
    int2 = int(num2)
    # get range of numbers between num1-num2
    range_list = list(range(int1, int2))
    # print(range_list)

    # splice array numbers into discrete integers (52 -> 5 2)
    for i in range(len(range_list)):
        new_ints = [int(x) for x in str(range_list[i])]
        # print(new_string)
        # print(new_ints)
        for num in new_ints:
            # check discrete integers against the number 5
            if 5 not in new_ints:
                # print numbers that do not contain 5
                print(f'{new_ints}\n')