# cook your dish here
for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    dic={}
    for i in lst:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    # If the value of the frequency must be diifernt in size of elements
    dic1={}
    for i in dic.values():
        if i not in dic1:
            dic1[i]=1
        else:
            dic1[i]+=1
    #return the maximum frequency
    m=max(dic1.values())
    l=[]
    # the count of elements who was having the same frequency must be return the min value
    for i in dic1:
        if dic1[i]==m:
            l.append(i)
    print(min(l))