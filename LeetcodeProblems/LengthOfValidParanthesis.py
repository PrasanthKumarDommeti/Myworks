def longestValidParentheses( s):
        stack =[-1] #It was initalized with -1 beacuse not an empty stack return  the values
        count=0
        for  i in range(len(s)):
            #If the element is left paranthesis then only we can append it 
            if s[i] == "(":
                stack.append(i)
            else:
                #If the same element was occuring Twice in a stack it will pop the first element
                stack.pop()
                if not  stack: #It was Right paranthesis it will be gives valid and append it into stack
                    stack.append(i)
                else:
                    # Poped countes must be caluclated in the count variable
                    count = max(count,i-stack[-1])
        return count
if __name__ =="main":
     s = "(()))"
     print(longestValidParentheses(s))