n=int(input())
p=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(p[i]==p[j] and i!=j):
            p[j]=1000;
    if(p[i]!=1000):
        print(p[i],end=" ")