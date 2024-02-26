from collections import Counter as Cn
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    # It will assign the frequency of each elements contained in the list
    d = Cn(l)
    f = 1
    for i in d:
        if d[i]&1:
            f=0
            break
    print('yes') if f else print('no')