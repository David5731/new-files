score = float(input("Enter student's score: "))

if score <= 100 and score >= 76:
    print("Excellent")
    
elif score <= 75 and score >= 70 and score:
    print('Very Good')
    
elif score <= 69 and score >= 65:
    print("Good")
    
elif score <= 64 and score >= 50:
    print("Credit")
    
elif score <= 49 and score >= 40:
    print("Pass")
    
else:
    print("Fail")