t=int(input())
while t>0:
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for each in l:
        d[each]=d.get(each,0)+1
    ans=float('inf')
    for each in l:
        if each^1 in d:
            ans=min(ans,n-d[each]-d[each^1])
        else:
            ans=min(ans,n-d[each])
    print(ans)
            
            
    t-=1