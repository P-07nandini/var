 #for loop
for i in range(5):
     print(i)

#break
for i in range (10):
    if i==5:
        break
    print(i)
    continue

for i in range(10):
     if i==6:
         continue
     print(i)

list=[10,20,30,40]
for i in list:
    print(i)
 #even
list=[2,3,4,5,6,7,8]
for i in list:
    if i%2==0:
        print(i)
 #odd
list=[2,3,4,5,6,7,9,8,15]
for i in list:
    if i%2!=0:
        print(i)
 #even number for n
n=int(input())
for i in range (n):
    if i%2==0:
        print(i)

 #positive
n=int(input())
for i in range (n):
    if i>0:
        print(i)

 #negative
n=int(input())
for i in range (-n,0):
        print(i)


 # 5th table
n=int(input())  
for i in range(1,11):
    print(f"{n} x {i}={n*i}")

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")


 # while loop
count=0
while count<5:
    print(count)
    count+=1
 # break 

# count=0
while count<21:
    if count==5:
        break
    print(count)
    count+=1


count=0
while count<20:
    if count==5:
        count+=1
        continue
    print(count)
    count+=1