n=input()
n=n.split()
x=n[-1]
w=min(x)
if w.islower():
    print(w)
else:
    q=w.lower()
    if q in x:
        print(q)
    else:
        print(w)
        