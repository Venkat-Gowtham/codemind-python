n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(1,n):
    if a[i]%2==0:
        continue
    else:
        s=1
        break
if s==0:
    print(True)
else:
    print(False)
