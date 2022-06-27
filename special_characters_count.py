n=input()
#print(n)
s="1234567890|!@#$%^&*(){}[]/\_.,:;"
c=0
for i in n:
    if i in s:
        c+=1
print(c)