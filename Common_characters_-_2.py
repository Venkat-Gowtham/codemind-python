s=input()
s=s.lower()
s=list(s.split())
f=s[0]
c=0
res=[]
for i in f:
    for j in s:
        if i not in j:
            break
    else:
        c+=1
print(c)