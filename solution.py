

user_input = input(f"please enter two numbers with space between \n")
string = sorted(user_input.split())
print(str(string))
inp_one = int(string[0])
inp_two = int(string[1])


numbers = []
while (inp_one <= inp_two ):
    numbers.append(inp_one)
    inp_one += 1


print (numbers)