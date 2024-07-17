import random
x = ["apple", "banana", "mango"]
print(x)

x = ("apple", "banana", "mango")
print(x)

x = ["apple", "banana", "mango"]
print(x)

x = {"Name": "Anarchy", "Clan": "Echelons"}
print(x)

x = frozenset({"apple", "banana", "mango"})
print(x)

x = b"hello"
print(x)

x = bytearray(5)
print(x)

x = 5.5
print(complex(x))

print(random.randrange(1, 100))

Fuel_Price = int(input("What's the new fuel price? "))
txt = f"the new fuel price is {Fuel_Price:.2f}"
print(txt)

Price_Per_Litre = float(input("How much is one litre of petrol? "))
Amount_Bought = float(input("How much fuel are you buying? "))
Litres_Bought = float(Amount_Bought / Price_Per_Litre)
print(Litres_Bought)

a = 0b1010
b = 0b1100
result = a & b
print(bin(result))

a = 0b1010
b = 0b1100
result = a | b
print(bin(result))

a = 0b1010
b = 0b1100
result = a ^ b
print(bin(result))

a = 0b1010
result = ~a
print(bin(result))

a = 0b1010
result = a << 2
print(bin(result))

a = 0b1010
result = a >> 2
print(bin(result))

guns = ["assault rifles", "Smg's", "Lmg's",
        "Marksman rifles", "Shotguns", "Sniper rifles"]
print(guns[2:6])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.append("orange")
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

guns = ["Assault rifle", "Smg's", "Shotgun",
        "Marksman rifle", "Sniper rifles", "Lmg's"]
i = 0
while i < len(guns):
    print(guns[i])
    i = i + 1
