number_grade = 76

if number_grade >= 80:
    print("A")
if number_grade >= 70:
    print("B")
if number_grade >= 60:
    print("C")
if number_grade >= 50:
    print("D")
if number_grade < 50:
    print("F")
# Prints B C D on seperate lines because 3 conditions are true

if number_grade >= 80:
    print("A")
if 70 <= number_grade < 80:
    print("B")
if 60 <= number_grade < 70:
    print("B")
if 50 <= number_grade < 60:
    print("B")
if number_grade < 50:
    print("F")

if number_grade >= 80:
    print("A")
elif number_grade >= 70:
    print("B")
elif number_grade >= 60:
    print("C")
elif number_grade >= 50:
    print("D")
elif number_grade < 50:
    print("F")

if number_grade >= 80:
    print("A")
elif number_grade >= 70:
    print("B")
elif number_grade >= 60:
    print("C")
elif number_grade >= 50:
    print("D")
else: 
    print("F")

def inspect_number(x):
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")

print(inspect_number(0))
