#Sliding the window problem
for _ in range(int(input())):
    n = int(input())
    s = input()
    if n<=3:
        print("YES")
    else:
        for i in range(n-3):
            # Always the size of the window must be at 4
            string = s[i:i+4]
            vow1 = 'a' in string or 'e' in string or 'i' in string 
            vow2 = 'o' in string or 'u' in string 
            # If not a vowel coming in the order print no
            if not vow1 and not vow2:
                print("NO")
                break 
        else:
            print("YES")
        
    
        