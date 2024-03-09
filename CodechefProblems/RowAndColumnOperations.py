n,q =map(int,input().split())
# Taken 2 empty list to solve the problem with size of the input
r=[0]*n
c=[0]*n 
maxi_r=0
maxi_c=0
for _ in range(q):
    x=input().split()
    if x[0] == "RowAdd":
        row=int(x[1])-1
        s=int(x[2])
        r[row]+=s
        maxi_r=max(maxi_r,r[row])
    else:
        col=int(x[1])-1
        s=int(x[2])
        c[col]+=s
        maxi_c=max(maxi_c,c[col])
print(maxi_r+maxi_c)