def f():
    n = int(input())
    a = sorted(list(map(int,input().split())))
    b = n*(n+1)//2 - sum(a)
    if b<0 or 1 not in a:
    
        return "Second"
    else:
        for j in range(n):
            if a[j]>j+1:
                return "Second"
    if b%2==0:
        return "Second"
    else:
        return "First"
t = int(input())
for i in range(t):
    print(f())