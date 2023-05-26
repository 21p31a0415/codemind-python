n=int(input())
lst=list(map(int,input().split()))
e=int(input())
c=0
for i in range(n):
    if lst[i]==e:
        c+=1
print(c)