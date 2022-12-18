n,k=map(int,input().split())
if (n>>k&1==1):
    print(n)
else:
    print(n+2**k)