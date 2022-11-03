n=int(input())
a=list(map(int,input().split()))
#print(*a)
r=a[0]
profit=0

for i in range(0,n-1):
    if a[i]>a[i+1]:
        continue
    else:
        profit+=a[i+1]-a[i]
        i+=1
print(profit)
    