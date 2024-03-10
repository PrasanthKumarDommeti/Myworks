for _ in range(int(input())):
    s=list(input())
    s.sort()
    power=0
    count=1
    for i in s:
        power += count*(ord(i)-96)
        count += 1
    print(power)