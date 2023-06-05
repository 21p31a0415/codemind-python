n=list(map(str,input().split()))
a=[]
for i in n:
    a.append((ord(max(i))-ord(min(i))))
print(sum(a))
    