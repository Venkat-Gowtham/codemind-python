n=int(input())
a=list(map(int,input().split()))
s=[]
i=0
j=n-1
while i<n//2 and j>=n//2:
    s.append(a[i])
    s.append(a[j])
    i+=1
    j-=1
if n%2!=0:
    s.append(a[n//2])
    s.append(0)
if len(s)==0:
    print(-1)
else:
    print(*s)
    