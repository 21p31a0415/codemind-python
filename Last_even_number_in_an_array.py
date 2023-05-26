n=int(input())
lst=list(map(int,input().split()))
for i in range(0,len(lst)):
    if lst[i]%2==0:
        even=lst[i]
print(even)