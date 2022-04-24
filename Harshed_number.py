n=int(input())
s=0
v=n
while n>0 :
    r=n%10
    s=s+r
    n=n//10
if(v%s==0) :
    print(True)
else :
    print(False)