
#pop()
#remove the return an elements from a dictionary given key
a={1:"mn","a":"op",3:"qr",4:"st"}
a.pop("a")
print(a)
#popiteam()
#remove the arbitary key-value pair from dictionaryand return it as tuple
d={1:"mn",2:"op",3:"qr",4:"st"}
d.popitem()
print(d)
# clear()
#the clear() method removes all items from the dictionary
d={1:"mn",2:"op",3:"qr",4:"st"}
d.clear()
print(d)


d={1:"mn",2:"abc",34:"390","ab":"cd","ef":234}
print(d.keys())
print(d.values())
print(d.items())

#b={1:"1",2:'4',3:"9",4:'16',5:'25',6:"36",7:'49',8:'64',9:'81'}
n = int(input())
d = {}
for i in range(n):
    a = int(input())
    d[a] = a * a
print(d)
# # 
# n=int(input())
# arr=[]
# for i in range(n):
#     a=input()
#     arr.append(a)
# d={}
# for i in arr:
#     if len(i)%2==0:
#         d[i]=len(i)
# print(d)

#frequency count
n=input()
d={}
for i in n:
    if i in d:
        d[i]=d.get(i,0)+12
    #     d[i]+=1
    # else:
    #     d[i]=1
print(d)

#uppercase to lowercase
n=int(input())
arr=[]
for i in range(n):
    a=input()
    arr.append(a)
d={}
for i in arr:
    val=i.upper()
    d[i]=val
print(d)

# n=int(input())
# d={}
# for i in range(n):
#     a=int(input())
#     d[a]=a%3
# print(d)

#ascii value
n=input()  #a b c    o/p:{'a': 97, ' ': 32, 'b': 98, 'c': 99}
d={}
for i in n:
    d[i]=ord(i)
print(d)

#amstrong nuber
n=int(input())
l=len(str(n))
temp=n
sum=0
while n!=0:
    r=n%10
    sum+=r**l
    n=n//10
if sum==temp:
    print("amstrong")
else:
    print("not amstrog")
