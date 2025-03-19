def outer():
    print("entering outer")
    
    def inner():
        print("entering inner")
        print("processing")
        print("leaving")
    return inner

ref=outer()
print("after calling outer")
ref()
print("program end")