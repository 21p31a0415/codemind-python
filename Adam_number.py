n=int(input())
s=n*n
sum1=0
sum2=0
while(n>0):
    w=n%10
    sum1=sum1*10+w
    n=n//10
s1=sum1*sum1
while(s1>0):
    a=s1%10
    sum2=sum2*10+a
    
    s1=s1//10
if(s==sum2):
    print("True")
else:
    print("False")