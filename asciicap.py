print("enter a char")
str=input()
newstr=''
i=0
while (i <= len(str)-1):
    data=str[i]
    ascii=ord(data)
    if (ascii>=97 and ascii<=122):
        newascii=ascii-32
        conchar=chr(newascii)
        newstr=newstr+conchar
        
    else:
        newstr=newstr+data
    i=i+1
print(newstr)