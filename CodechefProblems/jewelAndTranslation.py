for i in range(int(input())):
    j=input()
    s=input()
    ans=0
    jewel_set = set(j)
    for char in s:
        if char in jewel_set:
            ans += 1
    print(ans)