userInput = input("Please gimme two integers with a space inbetween!")

n1, n2 = userInput.split(" ")

n1 = int(n1)
n2 = int(n2)

for i in range(n1,n2+1):
    if("5" in str(i)):
        pass
    else:
        print(i)