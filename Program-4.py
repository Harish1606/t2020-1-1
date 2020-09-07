l=list(map(int,input().split(',')))
d={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(1,10):
    count=0
    for j in l:
        if j%i==0 and j>0:
            count+=1 
    d[i]=count
print(d)