# dish Recipe
from collections import Counter
testcase_no=int(input())
for testcases in range(testcase_no):
    n = int(input())
    # n,q = map(int,input().split())
    a = list(map(int, input ().split ()))
    d = list(map(int, input ().split ()))

    for i in range(n):
        a.append(d[i])
    f = Counter(a)
    ans = 0
    
    for i in f:
        ans = max(ans,f[i])
        
    print(ans)
        