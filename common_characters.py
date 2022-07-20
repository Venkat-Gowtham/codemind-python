s1=input().lower()
s2=input().lower()
s1=list(s1)
s2=list(s2)
res=[]
for i in s1:
    if i in s2 :
        if i not in res:
            res.append(i)
#print(res)
res=''.join(sorted(res))
res=res.strip()
if(len(res)>0):
    print(res)
else:
    print(-1)
