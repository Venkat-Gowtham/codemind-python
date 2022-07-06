n=input()
n=n.split()
q=""
x=0
y=0
for i in n:
    x+=ord(min(i))
for i in n:
    y+=ord(max(i))
print(abs(x-y))