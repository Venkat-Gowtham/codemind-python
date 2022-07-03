import math
n=int(input())
a=list(map(int,input().split()))
x=sum(a)
c=0
v=math.floor(x/n)
for i in a:
    if i>=v:
        c+=1
print(c)