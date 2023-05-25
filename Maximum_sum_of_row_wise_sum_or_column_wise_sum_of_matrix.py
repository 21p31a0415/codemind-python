r,c=map(int,input().split())
m=[]
n=[]
for i in range(r):
    lst=list(map(int,input().split()))
    m.append(lst)
    n.append(sum(lst))
for i in range(c):
    s=0
    for j in range(r):
        s=s+m[j][i]
    n.append(s)
print(max(n))