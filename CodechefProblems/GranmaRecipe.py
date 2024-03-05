t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    a1=set(list(a))
    b1=set(list(b))
    if(sorted(a1)==sorted(b1)):
        if(str(sorted(a)))==(str(sorted(b))):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    