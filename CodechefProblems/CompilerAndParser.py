for _ in range(int(input())):
    st = input()
    n = len(st)
    flag = False
    left = right = 0
    ans = 0 
    for i in range(n):
        if st[i] == "<":
            left += 1
            right += 1
            flag = True
        elif flag:
            left -= 1
        if left == 0:
            ans += 2 * right
            right = 0
        if left < 0:
            break
    print(ans)