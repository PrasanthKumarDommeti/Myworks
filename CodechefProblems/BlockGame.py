for _ in range(int(input())):
    N=int(input())
    sum =0
    temp = N  
    # Simply like a palindrome number  
    while(N > 0):
        r = N % 10 
        sum = (sum * 10) + r    
        N = N // 10   
    if(temp == sum):
        print("wins")
    else:
        print("loses")
    