a=10

def outer():
    b=20
    print(a)
    print(b)
    def inner():
        #nonlocal b                        #non local use case
        b=40
        c=30
        print(b)
        print(c)
        print(a)
    print(b)
    inner()
    print(b)
    
outer()
print(a)