# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1 = head
        for _ in range(k - 1):
            node1 = node1.next
        
        # Find the kth node from the end
        node2 = head
        length = 0
        while node2:
            node2 = node2.next
            length += 1
        node2 = head
        for _ in range(length - k):
            node2 = node2.next
        
        # Swap the values of the two nodes
        node1.val, node2.val = node2.val, node1.val
        
        return head

