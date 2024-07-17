import math
def Quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    Squareroot_of_discriminant = math.sqrt(discriminant)
    X1 = (-b + Squareroot_of_discriminant) / (2*a)
    X2 = (-b - Squareroot_of_discriminant) / (2*a)
    return X1, X2
X1, X2 = Quadratic(a = int(input("Enter a: ")) ,b = int(input("Enter b: ")), c = int(input("Enter c: ")))
if X1 is not None and X2 is not None:
    print(f"The solutions are: X1 = {X1}, X2 = {X2}")
else:
    print("The quadratic equation has no real roots.")