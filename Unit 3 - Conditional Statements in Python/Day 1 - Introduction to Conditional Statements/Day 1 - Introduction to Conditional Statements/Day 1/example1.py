number = int(input("Please enter a number: "))
if number > 0:
    print(f"{number} is a positive number")

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are eligible to vote")    
if age <= 18: 
    print("You are not eligible to vote")

str = input("Please enter a string: ")
if len(str) == 0:
    print("Your string is empty")
if len(str) > 0:
    print("Your string is not empty")

def max_number(a,b):
    if a > b:
        return a
    
    return b

print (max_number(4,5))
print (max_number(14,5))

def password_checker(password,user_input):
    if password == user_input:
        return True

    return False

pwd = input("Password: ")
secret = "gfddgfajutjhgdadg"

print(password_checker(pwd,secret))

def range_checker(number,lower,upper):
    if lower <= number <= upper:
        return True
    
    return False

a = int(input("Please input a number: "))
if range_checker(a,1,10):
    print("Good boy")

if range_checker(a,1,10) == False:
    print("BAD!")

print(range_checker(a,1,10))

def grade_converter(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "D"
    
    return "F"

