s1=input()
v=s1.lower()
res=v.split()
s2=input()
u=s2.lower()
h=u.split()
w=""
q=""
e=""
for i in res:
    for j in i:
        if j not in w:
            w+=j
for i in h:
    for j in i:
        if j not in q:
            q+=j
for i in w:
    if i not in q and i!=' ':
        e+=i
for i in q:
    if i not in w and i!=' ':
        e+=i
v=''.join(sorted(e))
print(v)

        
        