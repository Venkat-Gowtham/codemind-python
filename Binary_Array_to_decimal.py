n=int(input())
a=list(map(int,input().split()))
l=n-1
s=0
for i in a:
    s+=i*(2**l)
    l-=1
print(s)