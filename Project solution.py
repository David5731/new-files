#QUESTION 1 SOLUTION: 
def numbers(x,y,z):
    print(max(x,y,z))
numbers(x = int(input("Enter a number: ")), y = int(input("Enter a number: ")), z = int(input("Enter a number: ")))

#QUESTION 2 SOLUTION:
def sum_of_list():
      x = (8,2,3,0,7)
      print(sum(x))
sum_of_list()

#QUESTION 3 SOLUTION:
def multiplication_of_list(a,b,c,d,e):
      print(a * b * c * d * e)
multiplication_of_list(8, 2, 3, -1, 7)

#QUESTION 4 SOLUTION:
x = str(input("Enter a word: "))
print(x[::-1])

#QUESTION 5 SOLUTION:
def factorial(n):
    y = 1
    for x in range(1,num + 1):
        y *= x
    print(y)
num = int(input("Enter a number: "))
factorial(num)

#QUESTION 6 SOLUTION:
def given_range(n):
    if n in range(10):
        print("Number Present")
    else:
        print("Number Absent")
given_range(int(input("Enter a number: ")))

#QUESTION 7 SOLUTION:
x = str(input("Enter a word: "))
def user():
   upper = len([i for i in x if i.isupper()])
   print("The number of upper case is ", upper)
   lower = len([i for i in x if i.islower()])
   print("The number of lower is ", lower)
user()

#QUESTION 8 SOLUTION:
def distinct_elements(input_list):
    return list(set(input_list))
input_list = [1, 2, 2, 3, 4, 4, 5]
print(distinct_elements(input_list))

#QUESTION 9 SOLUTION:
def primenumberchecker(n):
    if n <= 1:
        print("Non prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Non prime number")
            return
    print("Prime number")
number = int(input("Enter a number: "))
primenumberchecker(number)

#QUESTON 10 SOLUTION:
def even_number_of_list():
      for x in range (2, 10, 2):
        print(x)
even_number_of_list()


#QUESTION 11 SOLUTION:
num = int(input("number: "))
newnum = []
def tired():
    for i in range(1,num):
        if num % i == 0:
            newnum.append(i)
    if sum(newnum) == num:
       print("perfect ")
    else:
       print("imperfect")
tired()

#QUESTION 12 SOLUTION:
def palindrome():
    x = str(input("Enter a word: "))
    y = x[::-1]
    if y == x:
        print("Palindrome")
    else:
        print("Non Palindrome")
palindrome()

#QUESTION 13 SOLUTION:
#Skip

#QUESTION 14 SOLUTION:
def pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for letter in alphabets:
        if letter not in sentence:
            return False
    return True
input_sentence = input("Enter a sentence: ")
if pangram(input_sentence):
    print("Pangram")
else:
    print("Not a Pangram")


#QUESTION 15 SOLUTION:
def sort_hyphenated_words():
    Input = input("Enter a hyphen-separated sequence of words: ")
    words = Input.split('-')
    words.sort()
    sorted = '-'.join(words)
    print("Sorted:", sorted)
sort_hyphenated_words()

#QUESTION 16 SOLUTION:
def square():
    tired = [i**2 for i in range(1,31)]
    print(tired)
square()

#QUESTION 17 SOLUTION:
#SKIP

#QUESTION 18 SOLUTION:
#SKIP

#QUESTION 19 SOLUTION:
def square():
    def Tired():
        print("Happy")
    Tired()
square()

#QUESION 20 SOLUTION:
#SKIP

#QUESTION 21 SOLUTION:
#SKIP