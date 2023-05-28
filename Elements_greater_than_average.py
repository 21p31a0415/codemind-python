n=int(input())
l=[int(i)for i in input().split()]
s=0
count=0
for ele in l:
    s=s+ele
avg=s//len(l)
for ele in l:
    if ele>=avg:
        count+=1
print(count)
