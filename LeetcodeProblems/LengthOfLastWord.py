def lengthOfLastWord(s):
        i=len(s)-1
        count=0
        #It can be used to negleted the spaces
        while i>=0 and s[i]==" " :
            i-=1
        #It can be used to calculated the word count
        while i>=0 and s[i]!=" " :
            count+=1
            i-=1
        return count

print(lengthOfLastWord("Hello world"))