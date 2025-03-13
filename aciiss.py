print("enter a char")
str=input()
newstr=''

i=0
while (i<=len(str)-1):
    data=str[i]
    ascii=ord(data)
    if (ascii>=65 and ascii<=90):
        newascii=ascii+32
        conchr=chr(newascii)
        newstr=newstr+conchr
    else:
        (ascii>=97 and ascii<=122)
        newascii=ascii-32
        conchr=chr(newascii)
        newstr=newstr+conchr
    i=i+1
print(newstr)
