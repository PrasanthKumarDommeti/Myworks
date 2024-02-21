def longestPalindrome(s):
        #When the string length is one that is also a valid palindrome
        if len(s)<=1:
            return s

        count=1
        msrt = s[0]
        #I can use brute force approaches with 2 pointers i & j 
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                # This can caluclated the substring with the reverse of the substring when we are calculated 
                if j-i+1>count and  s[i:j+1] == s[i:j+1][::-1]:
                    count=j-i+1
                    msrt = s[i:j+1]
                             
        # It must be return all palindromic strings in a row      
        return msrt

if __name__ == "__main__":
     print(longestPalindrome("babad"))
