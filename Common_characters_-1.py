s1=input().lower()
s1=s1.split()
r=s1[0]
res=[]
for i in r:
    for j in s1:
        if i not in j:
            break
    else:
        res.append(i)
if(len(res)>0):
    res=''.join(res)
    print(res)
else:
    print(-1)
