i = 1
while i < 10:
    print(i)
    i += 1
#THE ABOVE CODE LOOPS THROUGH THE COD TILL IT GETS TO 20

i = 15
while i < 20:
    print(i)
    if i == 17:
        break
    i += 1
#THE ABOVE CODE BREAKS THE LOOP WHEN IT GOT TO 17

i = 5
while i < 10:
    i += 1
    if i == 8:
        continue
    print(i)
#THE ABOVE SKIPS AN INPUTED NUMBER II THE LOOP

i = float(input("Enter a number less than 10: "))
while i < 10:
    print(i)
    i += 1
else:
    print("i is no longer less than 10")
    #TH ABOVE IS SELF EXPLANATORY