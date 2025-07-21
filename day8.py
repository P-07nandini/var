a="hello world "
b=" NICE TO MEET YOU  "
print(a.upper())#convert to upper case
print(b.lower())#convert to lower case
print(a.replace("hello","hi")) #replace hello with hi
print(b.strip())  #remove space from both ends
print(b.lstrip()) #remove space from left end
print(b.rstrip()) #remove space from right end
print(b.find("MEET")) #find the index id of "meet"
print(a.isalpha())  #check if all characters are alphabetic
print(a.title()) #cover to title case in 1st letter of each word

#slicing
# string slicing is a way to extract a part of a string using index positions.
# syntax:[start:end:step]
# start:index to begin slice
# end:index to end slice
# step: optional,step/jump size
a="hello world"
b="NICE TO MEET YOU"
print(a[0:7])# hello w
print(b[1::])# NICE TO MEET YOU
print(a[:5:])# hello
print(b[::2])# NITMEOU
print(a[1:9:2])# ello o
print(b[0:5])# NICE
print(a[0:5:2])# hlo
#revese slicing
print(a[-1::]) #d
print(a[:-3:])# hello wo
print(b[::-1])# UOY TEEM OT ECIN
print(b[-1:-5:-1])# UOY
print(b[-5:-1])#YOU

#tring functions
m="nandnipamidi"
print(len(m))#
print(type(m))
print(max(m))
print(min(m))
print(list(enumerate(m)))#index and value
print(sorted(m))
#middle substring
print(m[3:8])

#list slicing
# it is in python is a way to extract a portion from a list
# syntax:
# list[start:stop:end]
#list methods
#append
list=[1,2,3,4]
list.append([10,20])
print(list)

#extend
list=[1,2,3,4]
list.extend([10,20])
print(list)

#insert
list=[1,2,3,4]
list.insert(2,10)
print(list)

#remove
list=[1,2,3,4]
list.remove(2)
print(list)

#index
list=[1,2,3,4]
print(list.index(3))

#pop
list=[1,2,3,4]
list.pop(2)
print(list)

#clear
list=[1,2,3,4]
list.clear()
print(list)

#count
list=[1,2,3,4]
print(list.count(2))

#sort
list=[1,2,3,4]
list.sort()
print(list)

#reverse
list=[1,2,3,4]
list.reverse()
print(list)

#copy
list=[1,2,3,4]
list2=list.copy()
print(list2)

a=[0,1,2,3,4,5,6,7,8,9]
b=["a","b","c","d","e"]
print(a[-7:-2:2])
print(a[5:1:-1])
print(b[::2][1:])
print(a[-100:3])

