# # Introduction to strings 

# s = 'coffee'
# t = 'bread'

# print(s+t)     # Concatination 

# print(s[2])
# print(s[1:4]) 

# u = "123456789"
# a = u[2]
# b = u[6]
# print(a)
# print(b)
# print(a+b)     # Concatination 

# # Convert into integer 

# u = "123456789"
# a = int(u[2])
# b = int(u[6])
# print(a)
# print(b)
# print(a+b)


# s = "good"
# print(s * 5)     # good is printed 5 times
# print(s[0]*5)    # g is printed 5 times 

# x = "India"
# print(x == "India")
# print(x == "india")

# print("apple" > "one")   # a<o, o comes after a so "o" is bigger
# print("four" < "ten")    # t>f, t comes after f so "t" is bigger

print("ab" < "az")           # Since both words starting from "a" so it'll be measured from 2nd letter
print("abcdef" < "abcde")    # same here, No letter for f to compare with, so cannot be less than nothing     

s = "python"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

# Negative indexing 

print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

s = "qwertyuioiasdfghjkzxcvbnm"
# print(s[100])
print(len(s))
print(s[24])