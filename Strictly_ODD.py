n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]%2!=0:
        if i%2!=0:
            continue
        else:
            c=1
            break
if c==1:
    print(False)
else:
    print(True)
        