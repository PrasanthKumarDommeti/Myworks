# This can be solved by using Brute Force approaches
for _ in range(int(input())):
    n=int(input())
    a=[[int(x) for x in input().split()] for __ in range(n)]
    row=[0]*n
    column=[0]*n
    for i in range(n):
        for j in range(n):
            if a[i][j]==0:
                row[i]+=1
                column[j]+=1
    if 0 in row or 0 in column:
        print("NO")
    else:
        print("YES")