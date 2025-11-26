# Functions 

# def add(a,b):
#     ans1 = a + b
#     print(ans1)

# add(2,3)                   # Function call 
# add(5,6)                   #      ''
# add(8,9)                   #      ''


# def sub(a,b):
#     ans2 = a - b
#     print(ans2)

# sub(3,1)
# sub(8,6)
# sub(12,9)

# add(2,1) + sub(8,1)                     # Error, function calls can't be added like this , need to use 'return' to fix this 
# print( add(2,1) + sub(8,1) )            # Error, function calls can't be added like this 

# def discount(cost,d):
#     ans3 = cost-(cost*(d/100))
#     print(ans3)

# discount(100, 8)
# discount(1200, 8)
# discount(12123423, 18.5)

# add(17, 5)+sub(100, 50)+discount(1500, 8.5)    # Error 


# use return 

# When a function hits a return:
# It stops the function immediately
# It gives back a value
# That returned value can be:
#       -stored in a variable
#       -printed
#       -used inside another expression
#       -used inside another function 
#       -used in loops, conditions, etc.

# def add(a,b):
#     ans4 = a+b
#     return ans4 

# a = 2
# b = 15
# ans = add(a,b)+10
# print(ans)                # 27 



# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)             # 8 



def discount(cost,d):
    ans = cost - (cost*(d/100)) 
    return ans 

print("Enter the cost price")
x = int(input()) 

print("Enter the discount")
y = int(input()) 

print("The final discount:", discount(x,y))

