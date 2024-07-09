num = int(input("number: "))
newnum = []
for i in range(1,num):
    if num % i == 0:
        newnum.append(i)
if sum(newnum) == num:
        print("perfect ")
else:
    print("imperfect")
