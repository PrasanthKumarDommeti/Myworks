# cook your dish here
for i in range(int(input())):
    c = 0
    a,b = map(int,input().split())
    l=[]
    # Take the input strings in a list with lower convertions
    for i in range(a):
        l.append(input().lower())
    w1 = ""
    lst = "".join(l)
    # Direct spoon present in the list of strings
    if "spoon" in lst:
        print("There is a spoon!")
    else:
        for i in range(b):
            for j in range(a):
                w1+=l[j][i]
        if "spoon" in w1:
            print("There is a spoon!")
        else:
            print("There is indeed no spoon!")