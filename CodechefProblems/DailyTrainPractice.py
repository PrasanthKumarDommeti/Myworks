import math
X,N=map(int,input().split())
count=0
for _ in range(N):
    A=input()
    i,j=0,54
    for _ in range(9):
        L=A[i:i+4]+A[j-2:j]
        count+=math.comb(L.count('0'),X)
        i+=4
        j-=2
print(count)