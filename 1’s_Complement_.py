n=int(input())
s=""
while n>0:
    if n%2==0:
        s+='0'
    else:
        s+='1'
    n=n//2
s=s[::-1]
q=""
for i in s:
    if i=='0':
        q+='1'
    else:
        q+='0'
j=0
res=0
for i in range(len(q)-1,-1,-1):
    res+=int(q[i])*(2**j)
    j+=1
print(res)
        
