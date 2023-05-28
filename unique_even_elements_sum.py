n=int(input())
l=list(map(int,input().split()))
n=[]
s=0
for i in l:
    if i not in n and i%2!=1:
        n.append(i)
        s+=i
print(s)