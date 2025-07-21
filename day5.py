#def function
#arguments
#1 Positinal argument:

#2default arguments
def Hi(name="friends"):
    print("Hello",name)
Hi()
#3 keyword argument:
def Students(name,age):
    print("Name:",age)
    print("Age:",age)
Students(age=21,name="vijju")


#1.no arguments,no return value
def fun():
    print("keep smiling")
fun()
#2. with arguments,no return value
def greet(name):
    print("Hello",name)
greet("students")

#3 no arguments,with return value
def hi():
    return "friends"
value=hi()
print("wishes:",value)

#4 with argument and return value
def add(a,b):
    return a+b
result=add(2,5)
print("Sum:",result)