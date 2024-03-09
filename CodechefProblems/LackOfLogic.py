l=[]
for i in range(int(input())):
    s=input()
    s=s.upper()
    di={}
    for x in s:
        if x not in di:
            di[x]=1
    c=1
    for i in range(65,91):
        if chr(i) not in di:
            print(chr(i),end="")
            c=0
    if c==1:
        print("~",end="")
    print()
        