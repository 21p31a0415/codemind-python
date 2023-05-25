r,c=map(int,input().split())
lst=[list(map(int,input().split()))for i in range(r)]
for i in range(c):
    s=0
    for j in range(r):
        s+=lst[j][i]
    print(s,end=' ')