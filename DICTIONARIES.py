CODM = {
    "Guns": "Maddox",
    "Operators": "Manta ray",
    "Throwables": "Molotovs" 
}
#OR 
CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
print(CODM)

#ACCESSING FILES FROM THE DICT"
CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
X = CODM["Guns"]
print(X)
#OR:
CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
X = CODM.get("Operators")
print(X)
#THE ABOVE IS FOR GETTING THE VALUE OF A VARIABLE

CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
X = CODM.keys()
print(X)
#THE ABOVE IS USED FOR GETTING THE LIST OF VARIBLES

CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
X = CODM.values()
print(X)
#THE ABOVE IS USED FOR GETTING ALL THE OBJECTS IN THE VARIABLE.

CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
X = CODM.values()
CODM["Guns"] = "Hvk-30"
print(X)
#THE ABOVE IS USED FOR GENERATING AND ALSO CHNGING AN OBJECT IN A VARIABLE

CODM = dict(Guns = "Maddox", Operators = "Manta ray", throwables = "Molotovs")
if "Guns" in CODM:
    print("Guns is of the keys in this dictionary")
else:
    print("There's no such key in this dict")
#The above is self explanatory
#Learning Tip: The update function can also change the object carried by the variable
#AN EXAMPLE: CODM.update({"Guns": "AK 47"})
#LEARNING TIP: The update function is multi-purpose:
#It can both change the object in a variable and also add a whole variable in the list.
#AN EXAMPLE:

CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
CODM.update({"Throwables": "Molotovs"})
CODM.update({"Guns": "SMG'S"})
x = CODM
print(x)
#THE ABOVE IS AN EXAMPLE OF THE POWER OF THE UPDATE FUNC

CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
CODM.update({"Throwables": "Molotovs"})
CODM.update({"Guns": "SMG'S"})
x = CODM
x.pop("Throwables")
print(x)
# THE POP FUNCTION REMOVES THE SPECIFIED KEY("Throwables") AND OUTPUTS THE REST.
#THE popitem() FUNCTION REMOVES THE LAST KEY IN ADICTIONARY IN A CODE.

CODM =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del CODM
#THE ABOVE DELETES THE DICTIONARY USINGE THE del FUNCTION
#JUST LIKE THE update FUNCTION the del is also multi-putpose;
#MEANING THAT IT CAN BOTH DELETE THE WHOLE DICT AND DELETE A SPECIFIED KEY

CODM =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del CODM["brand"]
print(CODM)
#THE ABOVE DELETES THE KEY

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#THE ABOVE CODES WILL ONLY LEAVE THE DICT EMPTY

CODM = dict(Guns = "Assault rifle", Operators = "Manta ray")
for x in CODM:
    print(x)
CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
for x in CODM.keys():
    print(x)
#THE ABOVE LOOPS THROUGH THE LIST AND RETURNS THE KEYS

CODM = dict(Guns = "Assault rifle", Operators = "Manta ray")
for x in CODM:
    print(CODM[x])
#THE ABOVE PRINTS THE VALUES OF THE DICT
#OR:
CODM = dict(Guns = "Assault rifle", Operators = "Manta ray")
for x in CODM.values():
    print(x)
    
CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
for x,y in CODM.items():
    print(x,y)
#THE ABOVE USES THE items FUCNTION TO LOOP THROUGH AND PRINT BOTH THE KEY AND VALUE OF A DICT

CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
CODM2 = CODM.copy()
print(CODM2)
#THE ABOVE COPIES A DICTIONARY INTO ANOTHER
#OR:
CODM = dict(Guns = "assault rifle", Operators = "Manta ray")
CODM2 = dict(CODM)
print(CODM2)

#NESTED DICTONARIES:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

myfamily = {
    "Smith": {
        "father": "John",
        "mother": "Jane",
        "child": "Doe"
    },
    "Doe": {
        "father": "Alex",
        "mother": "Anna",
        "child": "Max"
    }
}
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
    