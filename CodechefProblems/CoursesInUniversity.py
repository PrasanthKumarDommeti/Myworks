for i in range(int(input())):
    a=int(input())
    lis=list(map(int,input().split()))
    n=max(lis)
    print(a-n)