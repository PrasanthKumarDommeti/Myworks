for _ in range(int(input())):
    n=int(input())
    s=input()
    count=0
    for i in range(0,n-1):
        # The order must be "10" sequencial form
        if s[i:i+2]=="10":
            count+=1
    print(count)