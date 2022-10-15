for k in range(int(input())):
    n=int(input())
    s=str(n)
    w=len(s)
    x=w-1
    res=0
    j=0
    f=[]
    while(x>=0):
        if j<3:
            res+=int(s[x])*(2**j)
            j+=1
        else:
            j=0
            f.append(res)
            res=0
            res+=int(s[x])*(2**j)
            j+=1
        x-=1
    f.append(res)
    for i in range(len(f)-1,-1,-1):
        print(f[i],end="")
    print()
        
        