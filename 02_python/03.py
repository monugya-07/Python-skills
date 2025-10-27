alpha = 'abcdefghijklmnopqrstuvwxyz'

# i = 10
# print(alpha[i])
# print(alpha[i+1])
# print(alpha[i+2])
# print(alpha[i+3])

# i = 30
# print(alpha[i%26])
# print(alpha[(i+1)%26])
# print(alpha[(i+2)%26])


s = 'sudarshan'

t = ''

print(alpha.index(s[0]))
print(alpha[(((alpha.index(s[0]))+1)%26)])
