n=int(input())
a=list(map(int,input().split()))
r=a[0]
price=0
for i in range(1,n):
    price=max(price,a[i]-r)
    r=min(r,a[i])
print(price)
    