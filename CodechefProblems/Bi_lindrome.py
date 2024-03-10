for _ in range(int(input())):
    a=int(input())
    l=input()
    if len(l)==len(set(l)):
        print("-1")
    else:
        print(a-2)
        
    