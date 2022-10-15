for k in range(int(input())):
    n=int(input())
    j=0
    r=0
    s=""
    while n>0:
        if n%2==0:
            s+="0"
        else:
            s+="1"
        n=n//2
    print(s[::-1])
    
            