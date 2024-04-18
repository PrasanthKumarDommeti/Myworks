class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        stack = []
        for c in s:
            # If there is a replacement of the character must be occured then you can pop() the element
            if stack and abs(ord(stack[-1])-ord(c))== 32:
                stack.pop()
            else:
                # Else the element must be poped in the stack
                stack.append(c)
        return "".join(stack)