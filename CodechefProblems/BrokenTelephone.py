for _ in range(int(input())):
    x=int(input())
    l = list(map(int,input().split()))
    s=[]
    for i in range(len(l)-1):
        # It was no allowing the duplicate elements in an order
        if l[i]!=l[i+1]:
            s.append(i)
            s.append(i+1)
    # returns the len must be the valid answer
    print(len(set(s)))