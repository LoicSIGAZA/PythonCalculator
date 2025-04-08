def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def UniGrade(score):
    if score < 40:
        return "F"
    elif 40 <= score < 50:
        return "D"
    elif 50 <= score < 60:
        return "C"
    elif 60 <= score < 70:
        return "B"
    else:
        return "A"
