class demo():
    def  swap(self,x,y):
        temp=x
        x=y
        y=temp
        
d=demo()


a=10
b=20
print("before swap")
print(a)
print(b)

d.swap(a,b)

print("after swaping")
a=10
b=20
print(a)
print(b)