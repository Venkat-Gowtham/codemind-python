n=int(input())
x=n-1
for i in range(n):
    for j in range(x):
        print(" ",end="")
    x-=1
    for j in range(i,0,-1):
        print(j,end="")
    print(0,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
        






















