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

fil=list(filter((lambda num:num%2==0),l))
print(fil)
