s=input()
count=0
for i in range(0,len(s)):
    if s[i].isupper():
        count+=1
print(count)