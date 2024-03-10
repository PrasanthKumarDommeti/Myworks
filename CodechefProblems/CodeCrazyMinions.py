t = int(input())
for i in range(t):
    s = input()
    min_instructions = 2      # when length of input = 1.
    for j in range(1,len(s)):
        temp = ord(s[j])-ord(s[j-1])        # using ascii values
        if temp<0:
            min_instructions += ((temp+26)+1)   # adding 26 if s[j]<s[j-1]
        else:
            min_instructions += (temp+1)      # 1 for instruction to print
            
    if min_instructions<=11*len(s):
        print("YES")
    else:
        print("NO")