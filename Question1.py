def fizzbuzz(max):
    for num in range (0, max):
        if(num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            print(num)
fizzbuzz(int(input("Enter a number: ")))