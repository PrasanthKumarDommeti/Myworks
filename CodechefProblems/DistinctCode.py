for _ in range(int(input())):
    s=input()
    i=0
    l=[]
    while i<len(s)-1:
        if s[i:i+2] in l:
            continue
        else:
            l.append(s[i:i+2])
        i+=1
    print(len(l))