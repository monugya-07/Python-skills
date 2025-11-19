# import random

# l = [1,3,4,67,18,17]
# l = random.sample(list(range(100)),100)

# sum = 0 

# for i in range(len(l)):
#     sum += l[i]
# print(sum)


# write a piece of code to find the dot product 

x = [1,2,3,4]
y = [5,6,7,8]

# dot_product = [(1*5) + (2*6) + (3*7) + (4*2)] 

sum = 0
for i in range(len(x)):
    sum = sum + x[i]*y[i]

print(sum)

