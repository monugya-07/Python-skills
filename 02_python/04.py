# Conditional statements 

birth_year = int(input("Please enter your birth year :"))

current_year = 2025

age = current_year - birth_year

if age>18 : 
    print("You're eligible for vote")
else :
    print("You're not eligible")

print("Good luck")  # This line will be printed in both if & else cases because it's outside


# Tutorial

# Problem 1 : Find whether the number given is odd or even ? Numbers : 4,5,0,-7,-10

print("Enter a number: ")
n = int(input())

if n % 2 == 0 : 
    print("Even")
else: 
    print("Odd")


# Problem 2 : Find whether the given number ends with 0 or 5 or any other number ? Numbers : 20,14,5,0,-27,-10

print("Enter a number : ")
n = int(input())

if n%5 == 0: 
    if n%10 == 0:
        print("Ends with 0")
    else : 
        print("Ends with 5")
        
else:
    print("Other")

# or

if n%5 == 0:
    if n%10 != 0:
        print("Ends with 5")
    else : 
        print("Ends with 0")
        
else:
    print("Other")


# Problem 3 : Find the grade of student based on the given marks from 0 to 100

n = int(input("Enter the marks: "))

if n>0 and n<60:
    print("E")
elif n>=60 and n<70:
    print("D")
elif n>=70 and n<80:
    print("C")
elif n>=80 and n<90:
    print("B")
elif n>=90:
    print("A")
else:
    print("Invalid input")

# or

a = int(input())

if(a >=0 and a<=100):
    if(a>=90):
        print("A")
    elif(a >= 80 and a < 90):
        print("B")
    elif(a >= 70 and a < 80):
        print("C")
    elif(a >= 60 and a < 70):
        print("D")
    elif(a < 60):
        print("E")
else:
    print("Invalid input")


