class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # we can return head when it contains only 1 element
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy  # We  can use directly as head


        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            # Increment current upto current.next
            curr = curr.next.next
        
        return dummy.next