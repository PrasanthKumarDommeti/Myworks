# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        f=[] # 2 stacks can be used to store the values of list in forward or backward orders
        r=[]
        temp = head
        while temp.next!=None:
            f.append(temp.val)
            temp = temp.next

        # These can be used to reverse the linked list by using 2 pointers when there is any chance
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        while temp.next!=None:
            r.append(temp.val)
            temp= temp.next
        if f == r:
            return True
        else:
            return False


        