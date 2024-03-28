'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # I am taking a pointer to traverse the list
    temp =None
    current = head
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    # The condition was used to check wheather it will traverse the last position or not
    if temp is not None:
        head = temp.prev
    # Simply we can return the head that will print the order by using the function
    return head