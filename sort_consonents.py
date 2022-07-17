def reverse(v):
    #print(s)
    temp=""
    f=0
    for i in range(len(v)):
        if v[i]!='a' and v[i]!='e' and v[i]!='i' and v[i] != 'o' and v[i]!='u' and v[i]!='A' and v[i]!='E' and v[i]!='I' and v[i]!='O' and v[i]!='U':
            temp+=v[i]
            f=1
    temp=''.join(sorted(temp))
    temp=str(temp)
    #print(temp)
    q=list(v)
    #print(q)
    x=0
    for i in range(len(q)):
        if q[i] != 'a' and q[i] != 'e' and q[i] != 'i' and q[i] != 'o' and q[i]!='u' and q[i]!='A' and q[i]!='E' and q[i]!='I' and q[i]!='O' and q[i]!='U':
            q[i]=temp[x]
            x+=1
    u=""
    for i in range(len(q)):
        u+=q[i]
    return u
s=input()
z=""
c=s.split()
for i in range(len(c)):
    z+=reverse(c[i])
    if i+1<len(c):
        z+=' '
print(z)
    
	

