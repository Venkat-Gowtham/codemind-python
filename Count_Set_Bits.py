n=int(input())
for i in range(n):
    x=int(input())
    c=0
    while x>0:
        if x%2!=0:
            c+=1
        x=x//2
    print(c)