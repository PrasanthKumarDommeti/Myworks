#It will as similar to minimum operations that must be needed to you
for _ in range(int(input())):
    x=input()
    a=x.count("0")
    b=x.count("1")
    if (a==1) or (b==1):
        print("Yes")
    else:
        print("No")