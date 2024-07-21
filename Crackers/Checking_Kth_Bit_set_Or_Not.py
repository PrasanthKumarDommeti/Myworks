def isKthBitSet(n: int, k: int) -> bool:
    # Write your code from here.
    bit_mask = 1 << (k - 1)  
    
    # Check if the K-th bit is set in N  
    return (n & bit_mask) != 0 
