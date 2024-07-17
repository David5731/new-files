cars = ["Ferrari","bugatti","Koenisegg"]
for x in cars:
    print(x)
#THE ABOVE PRINS OUT ALL THE KEYS IN THE LIST

for x in "ferrari":
    print(x)
#THE ABOVE PRINTS OUT AL THE LETTERS IN THE STRING

cars = ["Ferrari","bugatti","Koenisegg"]
for x in cars:
    print(x)
    if x == "bugatti":
        break
#THE ABOVE STOPS THE LOOP AT A GIVEN STRING

cars = ["Ferrari","bugatti","Koenisegg"]
for x in cars:
    if x == "bugatti":
        break
    print(x)
#THE ABOVE STOPS THE LOOP BEFORE THE GIVEN LOOP IS REACHED

cars = ["Ferrari","bugatti","Koenisegg"]
for x in cars:
    if x == "bugatti":
        continue
    print(x)
#THE ABOVE PRINTS OUT ALL LISTS EXCEPT THE GIVEN STRING

for x in range (8):
    print(x)
#THE ABOVE PRINTS OUT THE INCREMENTS OF A NMBER STARTING FROM 0

for x in range(2, 10):
    print(x)
#THE ABOVE LISTS OUT ALL NUMBERS FROM 2 TO 10

for x in range (2, 30, 2):
    print(x)
#THE ABOVE INCREMENTS THE SEQUENCE WITH 2 (THE DEFAULT IS 1)

for x in range(6):
  print(x)
else:
  print("Finally finished!")
#THE ABOVE PRINTS THE OUTCOME AND SAYS 'FINALLY FINISHED'

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.
Colors = ["Red", "Blue", "Black"]
Cars = ["Ferrari", "Bugatti", "BMW"]
for x in Colors:
  for y in Cars:
    print(x, y)
#THE ABOVE IS A NESTED LOOP

for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement

