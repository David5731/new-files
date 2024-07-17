def Myfunc(a,b):
    while a >= 0:
        print(a)
        a += 1
        if a == b:
            break
Myfunc(a=(int(input("Enter a number: "))), b=(int(input("Enter a number: "))))

for i in range (int(input("Enter a number: ")),int(input("Enter a number: "))):
    print(i)