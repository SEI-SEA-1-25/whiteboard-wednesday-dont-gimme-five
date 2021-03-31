def twoNums():
    # Ask for numbers
    num_one = int(input("Enter number one \n")) 
    num_two = int(input("Enter another number\n"))
    
    # print(num_one + num_two)

    num_list = []

    for i in list(range(num_one, num_two)):
        num_list.append(i)

    num_list.append(num_two)
    print(type(num_list))

    str_list = str(num_list)
    print(type(str_list))

    #Sort out list if number is equal to 5 or has 5 in it ⇣

    # for i in str_list:
    #     if index(i) in str_list == '5':
    #         del str_list[index(i)]
        
        



twoNums()









