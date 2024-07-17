def maximum(a, b, c, d):
    if a > b and a > c and a > d:
        f = a
    elif b > a and b > c and b > d:
        f = b
    elif c > a and c > b and c > d:
        f = c
    else:
        f = d
    print("The maximum number is:", f)
    return f
def minimum(a, b, c, d):
    if a < b and a < c and a < d:
        f = a
    elif b < a and b < c and b < d:
        f = b
    elif c < a and c < b and c < d:
        f = c
    else:
        f = d
    print("The minimum number is:", f)
    return f
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
max_value = maximum(a, b, c, d)
min_value = minimum(a, b, c, d)
def Range(max_value, min_value):
    x = max_value - min_value
    print("The range is:", x)
Range(max_value, min_value)