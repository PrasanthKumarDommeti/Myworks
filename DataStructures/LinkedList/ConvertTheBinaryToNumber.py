# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=''
        temp = head
        if head is None:
            return 
        while temp is not None:
            # I can store the nodes data into a string of "s" and using the concatenation operarions
            s+=str(temp.val)
            temp = temp.next
        # These function is used to return the binary into decimal format
        return  int(s,2)
        
        