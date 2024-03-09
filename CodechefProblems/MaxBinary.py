for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    if(s[0]=='1'):
        s=s+'0'*k
    else:
        if(len(s)>1):
            s='1'+s[1:]+'0'*(k-1)
        else:
            s='1'+'0'*(k-1)
    print(s)