class demo():
    def swap(self,x,y):
        temp=x
        x=y
        y=temp
        
        
d=demo()

a=10
b=20
print("before swaping")
print(a)
print(b)

d.swap(a,b)
print("after swaping")
print(a)
print(b)
