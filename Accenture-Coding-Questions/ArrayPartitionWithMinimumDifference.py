from typing import List
def minSubsetSumDifference(arr: List[int], n: int) -> int:
    """
    This function calculates the minimum absolute difference between subset sums.

    Args:
    arr (List[int]): A list of non-negative integers.
    n (int): The number of elements in the list.

    Returns:
    int: The minimum absolute difference between subset sums.
    """
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Create a dynamic programming table to store the subset sums
    dp = [[False for _ in range(total_sum // 2 + 1)] for _ in range(n + 1)]
    
    # Initialize the base case
    dp[0][0] = True
    
    # Fill the dynamic programming table
    for i in range(1, n + 1):
        for j in range(total_sum // 2 + 1):
            # If the current element is less than or equal to the current sum
            if arr[i - 1] <= j:
                # Choose the maximum of including or excluding the current element
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                # Exclude the current element
                dp[i][j] = dp[i - 1][j]
    
    # Find the maximum sum that is less than or equal to half of the total sum
    max_sum = 0
    for j in range(total_sum // 2, -1, -1):
        if dp[n][j]:
            max_sum = j
            break
    
    # Return the minimum absolute difference
    return total_sum - 2 * max_sum
