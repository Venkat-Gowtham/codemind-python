s=input()
q=[]
q=''.join(s)
v=list((q))
v=set(v)
if len(v)==len(s):
    print(True)
else:
    print(False)