a=int(input())
count=1;l=[] 
if a%2==0:
    a-=1 
for i in range(a):
    l.append(count)
    count+=2 
print(*l,sep=',')