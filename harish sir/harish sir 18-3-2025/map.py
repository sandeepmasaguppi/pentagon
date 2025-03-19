def data(num):
    return num+10

l=[]
i=0
while(i<=4):
    print("enter a value")
    res=int(input())
    l.insert(i,res)
    i=i+1
    
k=list(map(data,l))
print(k)