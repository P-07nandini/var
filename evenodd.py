n=int(input())
if n>0:
    for i in range(2,n+1,2):
        if i%2==0:
            print(i,end=" ")
else:
    for i in range(-2,n+1,-2):
            print(i,end=" ")

while True:
    a=input()
    if a=="exit":
        break
    print(a)