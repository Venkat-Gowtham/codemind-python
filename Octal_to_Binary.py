for k in range(int(input())):
    n=int(input())
    s=str(n)
    w=len(s)
    f=""
    for i in range(w):
        if i==0:
            if s[i]=='1':
                f+="1"
            elif s[i]=='2':
                f+="10"
            elif s[i]=='3':
                f+="11"
            elif s[i]=='4':
                f+="100"
            elif s[i]=='5':
                f+="101"
            elif s[i]=='6':
                f+="110"
            elif s[i]=='7':
                f+="111"
        else:
            if s[i]=="0":
                f+="000"
            if s[i]=='1':
                f+="001"
            elif s[i]=='2':
                f+="010"
            elif s[i]=='3':
                f+="011"
            elif s[i]=='4':
                f+="100"
            elif s[i]=='5':
                f+="101"
            elif s[i]=='6':
                f+="110"
            elif s[i]=='7':
                f+="111"
    print(f)
            
            
        
        
        
        