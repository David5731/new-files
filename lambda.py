x = lambda a : a + 15
print(x(float(input("Enter a number: "))))
#IT'S EASY 

x = lambda a, b, c, d , e : a * b * c * d * e
print(x(5, 6, 7, 8, 1))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(10))

def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(10))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(10))
print(mytripler(10))