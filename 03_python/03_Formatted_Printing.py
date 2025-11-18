# Formatted Printing

d = 1
m = 11
y = 2025

print("Today's date is", end = ' ')
print(d,m,y, sep = '-') 


n = int(input())
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    print(f'{n} x {i} = {n*i}') 
    print('{0}x{1} = {2}'.format(n,i,n*i))    # print using format function 
    print('%d x %d = %d' % (n, i, n*i))

pi = 22/7
print(f'Value of PI = {pi}')
print('Value of PI = {0}'.format(pi))
print('Value of PI = %f' %(pi))

pi = 22/7
print(f'Value of PI = {pi:2f}')
print('Value of PI = {0}'.format(pi))
print('Value of PI = %f' %(pi))

print('{0:5d}'.format(1))            # d stands for integer
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
