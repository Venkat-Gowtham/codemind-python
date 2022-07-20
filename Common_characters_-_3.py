s=input()
s=s.lower()
s=list(s.split())
f=s[0]
res=[]
for i in f:
    for j in s:
        if i not in j:
            break
    else:
        res.append(i)
res.sort()
res=''.join(res)
if len(res)>0:
    print(res[0])
else:
    print(-1)