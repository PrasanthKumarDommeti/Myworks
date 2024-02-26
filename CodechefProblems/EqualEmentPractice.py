for _ in range(int(input())):
    x=int(input())
    l = list(map(int,input().split()))
    # Used a Hashing to calculate the frequencies
    mp={}
    freq = 0
    for i in l:
        # This will calculated the frequency of each element in the array or list
        mp[i]=mp.get(i,0)+1
    for i in mp:
        if mp[i]>freq:
            freq = mp[i]
    if freq==1:
        print(len(l)-1)
    else:
        print(len(l)-freq)
    