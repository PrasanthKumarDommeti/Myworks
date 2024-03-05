from collections import Counter
for i in range(int(input())):
    n,q=map(int,input().split())
    s=list(input())[:n]
    # Counter should calculate the frequency of list of elements
    cot=Counter(s)
    for i in range(q):
        add=0
        c=int(input())
        # Iterating over values
        for j in cot.values():
            if c<j:
                add+=(j-c)
        print(add)    
    