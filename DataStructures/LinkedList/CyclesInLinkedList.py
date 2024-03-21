# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Baby & big are 2 pointers to iterate the values
        big = head
        baby = head    
        #Itterate one pointer and next element until it will reaches the null
        while big and big.next:
            # increment baby with one step and big was incremented by 2 steps
            baby, big = baby.next , big.next.next
            # wheather any of the case the cycle was found return True condition
            if  baby == big:
                return True
        return False
            
          
        


        