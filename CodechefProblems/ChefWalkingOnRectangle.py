import math
for _ in range(int(input())):
    n,m,k=[int(x) for x in input().split()]
    if (n==1 and m==1) or (n==1 and m==2) or (n==2 and m==1):
        print(0)
    elif n==1 or m==1:
        print(k)
    else:
        print(math.ceil(k/2))