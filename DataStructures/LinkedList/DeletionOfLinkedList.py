# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head1   
        # These can be using 2 pointers to locate the valuable adress and having same elements in list	
        prev, curr = temp, head
        while curr:
            # These can be used to calculate the remaining test case
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return temp.next
        