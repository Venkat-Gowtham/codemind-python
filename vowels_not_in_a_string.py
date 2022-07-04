n=input()
s="aeiou"
q=""
w=""
for i in n:
    if i in s and i not in q:
        q+=i
for i in s:
    if i not in q:
        w+=i
if len(w)==0:
    print(0)
else:
    x=" ".join(sorted(w))
    print(x)
        