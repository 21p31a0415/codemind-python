n=int(input())
a=list(map(int,input().split()))
b=int(input())
sum=0
for i in a:
    if i<=b:
        sum+=i
print(sum)