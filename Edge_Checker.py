n,p=map(int,input().split())
if(n-p==1 or p-n==1):
    print("Yes")
elif ((n==10 and p==1)or (p==10 and n==1)):
    print("Yes")
else :
    print("No")
    
