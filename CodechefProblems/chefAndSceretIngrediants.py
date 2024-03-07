for i in range(int(input())):
    n=int(input())
    l=[]
    # Makes my input string as set to elemenate duplicates
    for i in range(n):
        s=input()
        s=set(list(s))
        l.append(s)
    # First String may be a Stored in a variable
    a=l[0]
    for i in l[1:]:
        a=a.intersection(i)
    print(len(a))