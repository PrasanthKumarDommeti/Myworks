for _ in range(int(input())):
    x=int(input())
    arr= list(map(int,input().split()))
    odd=0
    even =0 
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    evens = len(arr)//2
    odd1 = len(arr)-evens
    sum = min(odd,evens)+min(even,odd1)
    print(sum)