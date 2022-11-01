n=int(input())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
s=0
for i in range(n):
    s+=a1[i]-b1[i]
if s<0:
    print(s*-1)
else:
    print(0)