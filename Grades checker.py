def evaluate_score():
    
    score = float(input("Enter student's score: "))
    
    if score <= 100 and score >= 76:
        return "Excellent"
    
    elif score <= 75 and score >= 70 and score:
        return'Very Good'
    
    elif score <= 69 and score >= 65:
        return "Good"
    
    elif score <= 64 and score >= 50:
        return "Credit"
    
    elif score <= 49 and score >= 40:
        return "Pass"
    
    else:
        return "Fail"
    
result = evaluate_score()
print(result)