for _ in range(int(input())):
    n = int(input())
    a =  sorted(list(map(int,input().split())))
    seta = set(x for x in set(a) if x != 0)
    print(len(seta))