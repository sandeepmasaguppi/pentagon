def even(num):
    if (num%2==1):
        return True
    else:
        return False
        



l=[]
i=0
while (i<=4):
    print("enter a number")
    data=int(input())
    l.insert(i,data)
    i=i+1
print(l)

i=0
while (i<=4):
    res=l[i]
    status=even(res)
    
    if(status==0):
        print(l[i])
    i=i+1

