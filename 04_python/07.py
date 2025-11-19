# Matrix multiplication 


r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim = 3 

# C[i][j] is the dot product of the i th row of A and the j th column of B 

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k]*B[k][j] 
print(C)


# Numpy will be discussed later briefly 

# import numpy

# X = numpy.mat(A)        
# Y = numpy.mat(B)

# print(X*Y)               # Converts into matrix form 

# In terminal it shows error because NumPy 2.0 removed numpy.mat(), it no longer works

# import numpy

# X = numpy.array(A)
# Y = numpy.array(B)

# print(X @ Y)

# or 

import numpy

X = numpy.asmatrix(A)
Y = numpy.asmatrix(B)

print(X * Y)
