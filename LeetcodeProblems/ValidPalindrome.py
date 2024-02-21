def isPalindrome(s):
    # Convert the combination of Upper and Lower into either Lower or Upper cases
    s=s.lower()
    # This command is used to elimenate the special characters
    k = ''.join(letter for letter in s if letter.isalnum())
    # Reverse the string and compare with the Original String
    if k == k[::-1]:
        return True
    else:
        return False
    
s="A man, a plan, a canal: Panama"
print(isPalindrome(s))

#Output : True