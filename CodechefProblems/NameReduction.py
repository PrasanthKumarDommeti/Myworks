for _ in range(int(input())):
    a_and_b=[x for x in input().split()]
    c=[input() for __ in range(int(input()))]
    parent_freq={}
    for i in a_and_b:
        for j in i:
            if j in parent_freq:
                parent_freq[j]+=1
            else:
                parent_freq[j]=1
    child_freq={}
    for i in c:
        for j in i:
            if j in child_freq:
                child_freq[j]+=1
            else:
                child_freq[j]=1
    for key,value in child_freq.items():
        if key not in parent_freq or parent_freq[key]<value:
            print("NO")
            break
    else:
        print("YES")