n=int(input())
r=0
for i in range(0,n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        r=i%10
        if(r==2 or r==3 or r==9) :
            c=c+1
    print(c)