def longest_common_pattern_length(str1, str2):
   
    count1 = {}
    count2 = {}

    
    for char in str1:
        count1[char] = count1.get(char, 0) + 1

    for char in str2:
        count2[char] = count2.get(char, 0) + 1

   
    common_chars = set(count1.keys()) & set(count2.keys())
    longest_common_length = sum(min(count1[char], count2[char]) for char in common_chars)

    return longest_common_length
        
            
        
for _ in range(int(input())):
    a = input()
    b = input()
    print(longest_common_pattern_length(a,b))
    