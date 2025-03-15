def fun1():
    print("inside  fun()")
    
def fun2(x,y):
    z=x*y
    print("res is", z)
    
fun1()

a=10
b=5
fun2(a,b)

str1=fun1


str2=fun2

str1()

str2(10,10)