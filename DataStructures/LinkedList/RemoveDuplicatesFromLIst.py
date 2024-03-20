# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        # If the list gone to be empty then return nothing
        if head is None:
            return 
        # If list contains elements then we can go for the comparision purpose and make the link
        while temp.next !=None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        # Return the head to iterate the process
        return head

        