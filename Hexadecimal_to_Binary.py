for i in range(int(input())):
    s=input()
    w=""
    for i in range(len(s)):
        if i==0 and s[i]=='0':
            continue
        else:
            if s[i]=='0':
                w+="0000"
            elif s[i]=='1':
                w+="0001"
            elif s[i]=='2':
                w+="0010"
            elif s[i]=='3':
                w+="0011"
            elif s[i]=='4':
                w+="0100"
            elif s[i]=='5':
                w+="0101"
            elif s[i]=='6':
                w+="0110"
            elif s[i]=='7':
                w+="0111"
            elif s[i]=='8':
                w+="1000"
            elif s[i]=='9':
                w+="1001"
            elif s[i]=='A':
                w+="1010"
            elif s[i]=='B':
                w+="1011"
            elif s[i]=='C':
                w+="1100"
            elif s[i]=='D':
                w+="1101"
            elif s[i]=='E':
                w+="1110"
            elif s[i]=='F':
                w+="1111"
    print(w)