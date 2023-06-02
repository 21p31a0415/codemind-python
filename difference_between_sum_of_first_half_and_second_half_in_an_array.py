n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(n//2):
    s1+=a[i]
for j in range(n//2,n):
    s2+=a[j]
print(s2-s1)