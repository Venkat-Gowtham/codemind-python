n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1,-1,-1):
    s+=a[i]
s=s//n
if a.count(s)>0:
    print(True)
else:
    print(False)