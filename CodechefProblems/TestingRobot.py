for _ in range(int(input())):
    x,y = map(int,input().split())
    s=str(input())
    k=list()
    # y can be the startung position so we need to firstly add the y into the List
    k.append(y)
    for i in range(len(s)):
        if s[i]=="R":
            k.append(k[i]+1)
            
        elif s[i]=="L":
            k.append(k[i]-1)
    # Set may be makes the element as uniquer     
    print(len(set(k)))
            
