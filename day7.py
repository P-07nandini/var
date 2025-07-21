#arguments
def fun(*args):
    for name in args:
        print("Hello",name)
    fun("vijju","nani","jannu")


def show(*args):
    print(args)
    for i in args:
        print(i)
show(1,2,3,4,5)


def show(*args):
    for item in args:
        print(item)
        #data=[1,2,3,4,5]
        show(1,2,4,3,6,4,6,9,3,5)

def student(**kwargs):
    print(kwargs)
student(name='znu',rol=29)