import math
n=int(input())
c=0
for i in range(n):
    if(pow(i,2)==n):
        print(True)
        c=1
        break
if(c==0):
    print(False)