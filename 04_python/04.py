# The obvious sort 

l = [4,32,6,87,54,3,30,6,87,8,76,5,13,6,4]

# l.sort()
# print(l)

x= []

min = l[0]

while(len(l)>0):
    min = l[0]
    for i in range(len(l)):
        if l[i]<min:
            min=l[i]
    
    x.append(min)
    l.remove(min) 

print(l)
print(x)
