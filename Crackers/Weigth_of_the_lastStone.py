import heapq  
import sys  

def weightOfLastStone(stones, n):  
    if n == 0:  
        return 0  # No stones  
    if n == 1:  
        return stones[0]  # Only one stone  

    # Create a max-heap (invert values for min-heap behavior)  
    max_heap = [-stone for stone in stones]  
    heapq.heapify(max_heap)  

    while len(max_heap) > 1:  
        # Get the two largest stones  
        first = -heapq.heappop(max_heap)  # The heaviest stone  
        second = -heapq.heappop(max_heap)  # The second heaviest stone  

        if first != second:  
            # If they are not equal, push the difference back to the heap  
            heapq.heappush(max_heap, -(first - second))  

    # If no stones are left, return 0; otherwise, return the last stone's weight  
    return -max_heap[0] if max_heap else 0  

# fast input function  
def takeInput():  
    n = int(input())  
    stones = list(map(int, input().strip().split(" ")))  
    return stones, n  

# main  
stones, n = takeInput()  
print(weightOfLastStone(stones, n))