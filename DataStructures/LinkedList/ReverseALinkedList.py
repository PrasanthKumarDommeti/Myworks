# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # This can be solved by using 2 pionter
        prev_node = None
        current_node = head

        while current_node is not None:
            # This can be used for 1 traversal
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        # Return the previous node to first last node
        return prev_node
       
        