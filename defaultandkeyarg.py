class disp():
    def swap(self,x=11,y=22,z=33):
        print(x,y,z)
        
        
d=disp()
a=10
b=20
c=30

d.swap(a,b,c)

d.swap(b,c)

d.swap(c)

d.swap(z=c)