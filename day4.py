#left angle triangle

n=int(input())
for i in range(1,n):
    print("*"*i)
#5to 1
n=int(input())
for i in range(n,0,-1):
    print("*"*i)

#right angle triangle
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i) +"*" * i)

#left to right(5-1)
n=int(input())
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)
#pyramid
n=int(input())
for i in range(1,n+1):
    print(" " *(n-1-i)+"* "*i)

#full square
n=int(input())
for i in range(1,n+1):
    print(*"*"*n)

#hollow squre
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" " ,end=" ")
    print()
    
#cross pattern
n= int(input())
for i in range(n):
    for j in range(n):
        if i==j or j+i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#number triangle
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()