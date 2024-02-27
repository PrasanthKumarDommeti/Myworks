x=int(input())
arr=list(map(int,input().split()))
count=0
m=0
for i in arr:
    if i !=0:
        count+=1
    else:
        count=0
    m = max(m,count)
print(m)

# Another solution you can count the length of the continues subarray