def output():
    print("inside outer")
    
    def inner():
        print("san ")
        
    return inner

ref=output
print(ref)

ref()