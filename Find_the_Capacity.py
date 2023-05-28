a,b,c=map(int,input().split())
c=2*a*b*c*512
k=c//1024
print(k,end='KB')