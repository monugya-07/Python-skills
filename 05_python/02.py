# Few functions on lists

def first_element(l):
    return l[0]

x = [1,2,3,4]

print(first_element(x)) 


def list_min(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i]<mini :
            mini = l[i]
    return mini 

def list_max(l):
    max = l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    return max

l = [2,3,4,5,1,6,7,8]
print(list_min(l))
print(list_max(l))


def list_appendBefore(l,z):
    newl = []
    for i in range(len(z)):
        newl.append(z[i])
    for i in range(len(l)):
        newl.append(l[i])
    return newl

def list_append(l,z):
    newl = [] 
    for i in range(len(l)):
        newl.append(l[i])
    for i in range(len(z)):
        newl.append(z[i])
    return newl 

l = [2,3,4,5,1,6,7,8]
z = [10,20,30]

print(list_appendBefore(l,z))            # [10, 20, 30, 2, 3, 4, 5, 1, 6, 7, 8] 
print(list_append(l,z))                  # [2, 3, 4, 5, 1, 6, 7, 8, 10, 20, 30] 


def list_average(l):
    sum = 0
    for i in range(len(l)):
        sum = sum+l[i]
    ans = sum/len(l)
    return ans 


print(list_average(l))

print(list_max([100,200,300,400,500]))    # Call function, this will be executed, all because of return value 

