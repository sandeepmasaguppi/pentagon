a=111

def fun1():
    global a
    a=11
    print(a)
    
    b=22
    print(b)
    
    
def fun2():
    global a
    a=54
    print(a)
    
    c=33
    print(c)


fun1()
print(a)
fun2()
print(a)

