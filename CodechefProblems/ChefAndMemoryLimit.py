for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a[0]
    for i in range(len(a)-1):
        # Previous memory allocation should be lesser then present allocation
        if a[i] < a[i+1]:
            # Removing higher from lowest to get the value
            b += a[i+1]-a[i]
    print(b)