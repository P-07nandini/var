#list comprehension 
# this code creates a list of squares of even numbers from 0 to 9
#list comprehension is a concise way to create lists using a single line of code.It replaces traditional loops and append() methods.
#syntax: [expression for item in iterable if condition]

#Squares
n=list(map(int,input("Enter a value:").split()))
square = [x**2 for x in n]
print(square)

#Input taken by user
#Print Even Numbers only
even= [x for x in n if x%2==0] #6
print(*even)
#Input taken by user print Even numbers only
n=map(int,input().split())
even = [x for x in n if x%2==0]
print(n)
#Print Even and Odd
odd = [x for x in n if x%2!=0]
print(*odd)
#Input taken by user print Even & Odd numbers

