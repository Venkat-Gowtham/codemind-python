n=int(input())
a=list(map(int,input().split()))
x=int(input())
for i in range(n-1,-1,-1):
    if a[i]==x:
        print(True)
        break
else:
    print(False)