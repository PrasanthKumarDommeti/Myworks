for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    if n==1:
        print("YES")
    else:
        max_a=0
        min_a=10**9+1
        for i in a:
            max_a=max(max_a,i)
            min_a=min(min_a,i)
        if max_a+min_a<=k:
            print("YES")
        else:
            print("NO")