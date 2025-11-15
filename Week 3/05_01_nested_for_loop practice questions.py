# Nested for loop


# Level 1

# Example : Print a rectangle of stars

for i in range(3):          
    for j in range(5):      
        print("*", end="")
    print()



# Example : Print numbers in a grid 

for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()



# Example : Multiply two numbers (Multiplication Table)

for i in range(1,11):
    for j in range(1,11):
        print(i," x ",j,' = ', i*j, end='\n')
    print()



# Print these pattern

# ****
# ****
# ****

for i in range(1,4):
    for j in range(1,5):
        print("*", end="")
    print()



# ****
# ****
# ****
# ****

for i in range(1,5):
    for j in range(1,5):
        print("*", end=" ")
    print()



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(1,4):
    for j in range(1,6):
        print(j, end=" ")
    print()



# AAA
# AAA
# AAA

for i in range(1,4):
    for j in range(1,4):
        print("A", end=" ")
    print()



# *
# **
# ***
# ****
# *****

for i in range(1,7):
    for j in range(1,i):
        print("*", end=" ")
    print()



# *****
# ****
# ***
# **
# *

for i in range(1,7):
    for j in range(1,7-i):
        print("*", end=" ")
    print()



# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()



# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end="")
    print() 



# 10101
# 01010
# 10101
# 01010

rows = 4
cols = 5

for i in range(rows):
    for j in range(cols):
        print((i + j) % 2, end="")
    print()



# Level 2 nested loops

# *****
# *   *
# *   *
# *   *
# *****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols - 1:
            print("*", end = "")
        else:
            print(" ", end="")
    print()


#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*", end="")
    print()


# 12345
# 1234
# 123
# 12
# 1

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j, end="")
    print()


# *****
#  ****
#   ***
#    **
#     *

for i in range(1,6):
    for j in range(1,i+1):
        print(" ", end='')
    for k in range(1,6-i+1):
        print("*", end="")
    print()


#     *
#    ***
#   *****
#  *******
# *********

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")
    print()