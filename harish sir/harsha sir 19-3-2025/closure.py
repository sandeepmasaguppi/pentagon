def outer():
    print("outer fun")
    
    def inner():
        print("inner")
    return inner
    
ref=outer()
print(ref)
ref()