user_input = input('Please choose a number')
user_input = int(user_input)

for i in range(user_input):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('fizz, buzz')
    else: 
        print(user_input, '😍')