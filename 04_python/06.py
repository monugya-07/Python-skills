# Matrix Addition 


dim = 3

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

# C = [[],[],[]]                   # It won't work

for i in range(dim):
    for j in range (dim):
        C[i][j] = A[i][j] + B[i][j]   # Matrix representation: A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] 
                                      #                     A[0] = [1,2,3], A[1] = [4,5,6], A[2] = [7,8,9]
                                      #                  A[i][j] == A[0][0] = 1, A[0][1] = 2, A[0][2] = 3 
print(C)



# Multiplication of matrix, It multiplies the numbers but this is not the way

for i in range(dim):
    for j in range (dim):
        C[i][j] = A[i][j] * B[i][j]
print(C)

