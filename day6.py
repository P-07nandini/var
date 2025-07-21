#call by value
def fun(x):
    x=x+5
    print("Inside of function:",x)
a=20
fun(a)
print("Outside function:",a)
#call by reference
def fun(my_list):
    my_list.append(99)
    print("Inside function:",my_list)

numbers=[1,2,3,4]
fun(numbers)
print("outside function:",numbers)


# lambda function
#Syntax: lambda arguments:expression 
a=lambda x,y:x+y
print(a(10,20))
#no arguments
b=lambda : "hello!"
print(b())
#one arguments
s=lambda x:x*x
print(s(5))

#lambda map()FUNCTION
N=[1,2,3,4,6,7,8]
S=list(map(lambda x:x*x,N))
print(S)

#convert to uppercase
names=['yuvi','lucky','nani']
upper_names=list(map(lambda x:x.upper(),names))
print(upper_names)

#scope
def hi():
    name="nani"
    print("hello",name)
hi()
#print(name) X error:name not defined

#global scope
x=10
def show():
    print(x)
show()
print(x)


#outer function
def fun():
    x=10
    def inner():
        nonlocal x
        x+=5
        print("inner:",x)
    inner()
    print("outer:",x)
fun()