def fun1():
    print("call fun")
    
def fun2(x,y):
    z=x+y
    print("res is",z)

def display(ptr3,ptr4):
    ptr3()
    ptr4(20,20)
    
fun1()
a=10
b=20
fun2(a,b)

ptr1=fun1

ptr2=fun2

ptr1()
ptr2(10,40)

display(ptr1,ptr2)

