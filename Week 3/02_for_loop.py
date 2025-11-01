
for i in range(10):
    print(i, 'Monugya Borchetia') 



for i in range(10):
    if i%2 == 0:
        print(i, 'Monugya Borchetia') 
    else:
        print(i, "Hi World !")


n = int(input())

for i in range(10):
    if i%2 == 0:
        print(i, 'Monugya Borchetia') 
    else:
        print(i, "Hi World !")


n = int(input())

ans = 0
for i in range(n):
    ans = ans+i

print(ans)

n = int(input())
for i in range(11):
    print(n,'x',i,'=',n*i)

n = int(input())
for i in range(5,11):
    print(n,'x',i,'=',n*i)

for i in range(1,11):
    if(i%2==0):
        print(i)

for i in range(1,11):
    if(i%2!=0):
        print(i)

for i in range(1,11,2):      # Step parameters ( increment by 2 )
    print(i)

for i in range(10):          # (0,10,1) 
    print(i)

for i in range(9,-1,-1):      
    print(i)


# for loop without range ( for each )

country = "India"
for i in country:
    print(i)
   
for i in range(10):        # ( End with )
    print(i, end = ' ')




