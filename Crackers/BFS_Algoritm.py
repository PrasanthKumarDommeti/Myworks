from typing import List  
from collections import deque  

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:  
    # Initialize a queue for BFS and a list to track visited nodes  
    queue = deque([0])  # Start from vertex 0  
    visited = [False] * n  # Mark all nodes as unvisited  
    visited[0] = True  # Mark the starting node as visited  
    traversal_order = []  # This will hold the BFS traversal order  
    
    while queue:  
        # Dequeue a vertex from the queue  
        current_vertex = queue.popleft()  
        # Add this vertex to the BFS traversal order  
        traversal_order.append(current_vertex)  

        # Iterate over all neighbors of the current vertex  
        for neighbor in adj[current_vertex]:  
            if not visited[neighbor]:  
                visited[neighbor] = True  # Mark neighbor as visited  
                queue.append(neighbor)  # Enqueue the neighbor  
    
    return traversal_order  

