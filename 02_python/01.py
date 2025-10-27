a = 10
print(type(a))

#Dynamic typing 

a = "India"
print(type(a))


# Keywords cannot be defined as variable names
# 1a is not a valid variable name, can't be started with a number

n = 10
print(type(n))
n = n/2           # or n/1, Float
print(type(n))
print(n)          # Float


# Multiple assignment 

x,y = 1,2
print(x,y)

x = y = z = 10
print(x,y,z)


# Swap the value of the variable with each other 

x,y = y,x
print(x,y)

x = 10
print(x)
del(x)     
# print(x)      # Error ( file deleted ) 

count = 0
count+=1
count+=1
count+=1
count+=1
print(count)

c = 10
c-=1
c-=1
c-=1
print(c)

d = 10
d*=2
d*=2
d*=2
print(d) 


# 'in' operator

print('alpha' in "A variable name can only contain alpha-numeric characters and underscores")
print('alpha' in "A variable name must start with a letter or the underscore character")


# chanining operator -> Multiple relational operator 

x = 5
print(1 < x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4) 

# Escape characters(somtime later)

# \t = tab = gap = multiple spaces 

print("I'm Monugya \t I'm from Assam")

print("I'm Monugya \nI'm from Assam ")   # Next line 