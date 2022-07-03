n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(1,n):
    if a[i]==0 or a[i]==1:
        continue
    else:
        s=1
        break
if s==1:
    print(False)
else:
    print(True)