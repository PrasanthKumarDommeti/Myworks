for _ in range(int(input())):
    n = int(input())
    s = input()
    l = len(s)
    if s[l-1] in s[0:l-1]:
        print("YES")
    else:
        print("NO")