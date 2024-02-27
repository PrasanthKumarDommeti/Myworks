arr=list(map(int,input().split()))
if x==1:
    print(l[0])
m,l,mi = 1,1,0
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        l+=1
    else:
        if m<l:
            m=l
        l=1
if m<l:
    m=l
    # If you wants only length then  print m is sufficient
    mi = n-m
# If you want the array sequence using the statement also
for i in range(mi,(m+mi)):
    # The continues array sequrnce without zeros else you can remove the if condition and print it 
    if arr[i]>0:
        print(arr[i],end=" ")