s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
s1.discard(' ')
s2.discard(' ')
a=s1.symmetric_difference(s2)
b=[]
for i in a:
    if i!=" " and i.isalpha():
        b.append(i)
b.sort()
print("".join(b))
        