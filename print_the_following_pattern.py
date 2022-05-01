n=int(input())
b=n
a=1
while(b>0):
    for i in range(a,n+1) :
        print(i,end="");
    print();
    n=n-1;
    b=b-1;