


question = input('Give me two numbers\n')

def sort(question):
    x = []
    numbers = question.split(' ')
    for number in numbers:
        x.append(number)  
        # int(number)
        # print(type(numbers))
    print(x)
    a = range(int(x[0]), int(x[1])+1)
    for n in a:
        if "5" in str(n):
            pass
        else:
            print(n)

sort(question)