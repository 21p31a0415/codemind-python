m,n=map(int,input().split())
l=[list(map(int,input().split()))for i in range(m)]
s=0
for i in range(n):
    for j in range(m):
        if(i==0):
            s+=l[i][j]
        elif(i==n-1):
            s+=l[i][j]
        elif(j==0):
            s+=l[i][j]
        elif(j==m-1):
            s+=l[i][j]
print(s)