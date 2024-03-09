for _ in range(int(input())):
    n = int(input())
    s = input()
    pairs = s.count('11')
    if '1' in s:
        if pairs > 0:
            print(2)
        else:
            print(1)
    else:
        print(0)