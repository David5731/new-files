def Max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
def Min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
def Range(numbers):
    maximum = Max(numbers)
    minimum = Min(numbers)
    return maximum - minimum
numbers = []
while True:
    Input = input("Enter a number (or 'stop' to finish): ")
    if Input.lower() == 'stop':
        break
    try:
        number = int(Input) 
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please, Enter a valid number.")
if numbers:
    print("Numbers entered:", numbers)
    print("Maximum value:", Max(numbers))
    print("Minimum value:", Min(numbers))
    print("Range:", Range(numbers))
else:
    print("No numbers were entered.")