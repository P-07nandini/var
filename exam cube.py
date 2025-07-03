# 1
'''m=int(input("enter value"))
n=int(input("enter value"))
total=0
for i in range(m,n+1):
    cube=i**3
    total+=cube
print(total)

#2
d=int(input())
bonus=100
score=0
if d>250:
    score+=(d-250)*10
    d=250
if d>200:
    score+=(d-200)*8
    d=200
if d>100:
    score+=(d-100)*6
    d=100
if d>50:
    score+=(d-50)*5
    d=50
if d>0:
    score+=(d-0)*3
    score+=bonus
    print(score)
    
#7
num=int(input())
for i in range(0,num+1):
    if i%2==0:
        print(i,"EVEN")
    else:
        print(i,"ODD") '''
 #3

n=int(input())
m=int(input())

for i in range(n,m):
    total=n**m
print("armstrong")