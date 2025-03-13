print("enter a char")
str=input()
newstr=''
i=0
while (i <= len(str)-1):
    data=str[i]
    ascii=ord(data)
    if (ascii>=65 and ascii<=90):
        newascii=ascii+32
        conchar=chr(newascii)
        newstr=newstr+conchar
    else:
        newascii=ascii-32
        conchar=chr(newascii)
        newstr=newstr+conchar
   
    i=i+1
print(newstr)
