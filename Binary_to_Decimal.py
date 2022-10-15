for k in range(int(input())):
    n=int(input())
    s=str(n)
    w=len(s)
    f=""
    j=0
    r=0
    for i in range(w-1,-1,-1):
        r+=int(s[i])*(2**j)
        j+=1
    print(r)
            
            
        
        
        
        