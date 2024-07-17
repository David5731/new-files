def func():
    print("Skill Issues")
func()
#THE ABOVE CALLS OUT MY FUNCTION

def func1(First_name):
    print(First_name + " Loko")
func1("Tosin")
func1("Daniel")
func1("Ayomide")
#THE ABOVE IS SELF EXPLANATORY

def func3(First_name, Last_name):
    print(First_name + " " + Last_name)
func3("Tosin", "Loko")
#I CAN'T PUT IT TO WORDS,IT'S SELF EXPLANATORY

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#USED TO AVOID BUGS

def Children(Child1, Child2, Child3):
    print("The youngest child is " + Child3)
Children("Funke", "Faith", "Folake")
#THE ABOVE CODE IS EASY

def Kids(**kids):
    print("Your first name is " + kids["First_name"])
    print("Your last name is " + kids["Last_name"])
    print("Your full name is " + kids["First_name"],  kids["Last_name"])
Kids(First_name = str(input("Enter your first name: ")), Last_name = str(input("Enter your last name: ")))
#THE ABOVE CODE TAKES YOUR FUST AND LAST NAME AS INPUT TO GET YOUR FULL NAME

def Origin(country = "Asgard"):
  print("I am from " + country)
Origin("Sweden")
Origin("India")
Origin()
Origin("Brazil")
#THE ABOVE INPUTS YOUR def AS THE KEY FOR def WITHOUT AN INPUT

def func4(food):
    for x in food:
        print(x)
fruits['apple','mango','cherry']
func4(fruits)
#THE ABOVE IS SELF EXPLANATORY

def numbers(x):
  return  10 * x
print(numbers(3))
print(numbers(5))
print(numbers(9))
#THE ABOVE IS SELF EXPLANATORY

def myfunction():
  pass
# having an empty function definition like this, would raise an error without the pass statement

def my_function(x, /):
  print(x)
my_function(3)
#I DON'T EVEN KNOW

def my_function(x):
  print(x)
my_function(x = 3)

def my_function(*, x):
  print(x)
my_function(x = 3)
#SAME AS LINE 61 TO 63

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

