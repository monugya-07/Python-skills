# import random

# l = []

# for i in range(1000):
#     l.append(random.randint(1,100))
# print(l)


# import random

# l = [1,2,3,4,5,6,7,8,9,11,13,22,3,4,75]
# a = 567172

# flag = 0

# for i in range(len(l)):
#     if a == l[i]:
#         print("Found")
#         flag = 1
#         break
# if flag == 0:
#     print("Not found")



# import random

# l = []

# for i in range(1000):
#     l.append(random.randint(1,100))
# print(l)

# a = l[i]

# flag = 0

# for i in range(len(l)):
#     if a == l[i]:
#         print("Found")
#         flag = 1
#         break
# if flag == 0:
#     print("Not found")



# import random

# l = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# n = 0
# while n>-1:
#     print("Enter a year : ")
#     n = int(input())

#     flag = False

#     for i in range(len(l)):
#         if n==l[i]:
#             print("Element found")
#             flag = True
#             break
#     if n == -1 :
#         print("Exit") 
#     else: 
#         print("Not found")   
    
    

import random

l = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

n = 0
while n>-1:
    print("Enter a year : ")
    n = int(input())

    flag = False

    for i in range(len(l)):
        if n==l[i]:
            print("Element found")
            flag = True
            break
    if flag == False:
        print("Not found")    
     
    

