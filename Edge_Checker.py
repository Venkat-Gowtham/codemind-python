a,b=map(int,input().split())
if (a==10 and b==1) or (b==10 and a==1):
    print("Yes")
elif abs(a-b)==1:
    print("Yes")
else:
    print("No")
    