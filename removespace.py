str="      hi    i     am     "
print(str)
str1=str.lstrip()
print(str1)
str2=str.rstrip()
print(str2)
str3=str.strip()
print(str3)

print("enter a string")
str=input()
i=0
newstr=""
while (i<=len(str)-1):
    data=str[i]
    if (data==' '):
        i=i+1
    else:
        newstr=newstr+data
        i=i+1
print(newstr)