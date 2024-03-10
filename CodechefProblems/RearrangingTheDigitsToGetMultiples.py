for i in range(int(input())):
    x = int(input())
    y = list(map(int,input()))
    ans=''
    for i in y:
        if i%5==0:
            ans = "Yes"
            break
        else:
            ans ="No"
    print(ans)
    
    
    
    