def outer():
    print("entering outering")
    
    def inner():
        print("entering inner")
        print("procesing")
        print("leaving inner")
        
    print("calling inner")
    inner()
    
outer()
print("pgm code")  