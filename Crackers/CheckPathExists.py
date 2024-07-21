from os import *
from sys import *
from collections import *
from math import *

def checkPathExists(v, e, source, destination, edges):
    # Write your code here
    # Return a Boolean
    graph = [[] for _ in range(v)]  
    for edge in edges:  
        graph[edge[0]].append(edge[1])  
    
    # Step 2: Perform BFS to check if a path exists  
    queue = deque([source])  
    visited = set([source])  
    
    while queue:  
        node = queue.popleft()  
        
        # If we reach the destination  
        if node == destination:  
            return True  
        
        # Visit all adjacent nodes  
        for neighbor in graph[node]:  
            if neighbor not in visited:  
                visited.add(neighbor)  
                queue.append(neighbor)  
                
    # If we exhaust all possibilities and don't find the destination  
    return False  
