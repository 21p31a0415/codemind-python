n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
n=[]
for i in l:
    if i>=a and i<=b:
        n.append(i)
if len(n)==0:
    print('-1')
else:
    print(min(n))