# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        first = temp 
        last = temp
        # Itterate the first upto the n value reaches
        for _ in range(n+1):
            first = first.next
        while first is not None:
            first = first.next
            last = last.next
        # When the first must be reaches None then we can connect the last indexes
        last.next = last.next.next
        # return head when temp.next has head
        return temp.next

        