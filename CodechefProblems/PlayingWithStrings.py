for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    zeros_s = s.count('0')
    zeros_r = r.count('0')
    if zeros_s == zeros_r:
        print('YES')
    else:
        print('NO')