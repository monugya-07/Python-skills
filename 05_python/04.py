# Matrix multiplication using Function 

def initialize_mat(dim):
    c = []
    for i in range(dim):
        c.append([]) 
    for i in range(dim):
        for j in range(dim):
            c[i].append(0) 
    return c 
