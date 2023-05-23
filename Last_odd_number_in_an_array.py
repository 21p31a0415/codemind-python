n=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
    if lst[i]%2==1:
        odd=lst[i]
print(odd)
