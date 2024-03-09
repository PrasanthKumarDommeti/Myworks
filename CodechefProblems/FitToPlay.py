for i in range(int(input())):
    n=int(input())
    x=[int(x) for x in input().split()]
    maximum=0
    minimum=x[0]
    for k in range(len(x)):
        if x[k]<minimum:
            minimum=x[k]
        diff=x[k]-minimum
        maximum=max(maximum,diff)
    if maximum==0:
        print("UNFIT")
    else:
        print(maximum)