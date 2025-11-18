l = [1,2,3,4,5,6,7,10] 
print(l)

l.append(100)
print(l)

l.append(2)
print(l)

l.remove(100)
print(l)

l.remove(2)
print(l)                 # It removes first '2' 


l = []

l.append(1)
l.append(2)
l.append(3)

print(l)                  # [1, 2, 3] 

x = []

x.append(l)
print(x)                  # [[1, 2, 3]] 

m = [10,20,30]

x.append(m)
print(x)                  # [[1, 2, 3], [10, 20, 30]] 

t = []

t.append(x)
print(t)                  # [[[1, 2, 3], [10, 20, 30]]] 

t.append([100,101,102])  
print(t)                  # [[[1, 2, 3], [10, 20, 30]], [100, 101, 102]]


n = []
n.append([1,2,3])
n.append([4,5,6])
n.append([7,8,9])

print(n)                  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
print(n[0]) 
print(n[0][0])            # 1 
print(n[1][2])            # 6 


