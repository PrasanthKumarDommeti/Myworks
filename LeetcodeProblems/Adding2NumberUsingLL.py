# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create an empty Node
        dummy = ListNode()
        res = dummy

        total = carry = 0
        # All are False then return result
        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            #Simply i am decreasing the count
            num = total % 10
            carry = total // 10
            # Itterate the list
            dummy.next = ListNode(num)
            dummy = dummy.next
        # Returning the result.next value
        return res.next