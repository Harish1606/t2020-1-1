a=int(input())
l=[];count=1 
for i in range(a):
    l.append(count)
    count+=2 
print(*l,sep=',')