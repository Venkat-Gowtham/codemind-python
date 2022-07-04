n=input()
n=n.split()
c=0
x=0
q=""
for i in n:
    c+=1
#print(c)
for i in n:
    if x<c:
        if x%2==0:
            q+=i[::-1]
        else:
            q+=i
    if x+1<c:
        q+=' '
    x+=1
print(q)        
