n=int(input())
a=list(map(int,input().split()))
q=[]
for i in a:
    if i%2!=0:
        q.append(i)
for i in a:
    if i%2==0:
        q.append(i)
print(*q)