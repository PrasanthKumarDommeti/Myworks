def twoSum(arr, target, n):
    # Sort the array
    arr.sort()

    # Initialize the result list to store pairs
    ans = []

    # Initialize two pointers
    start = 0
    end = n - 1

    # Loop until the start pointer is less than the end pointer
    while start < end:
        # If the elements at start and end sum up to the target
        if arr[start] + arr[end] == target:
            # Add the pair to the result list
            ans.append((arr[start], arr[end]))
            start += 1  # Move the start pointer forward
            end -= 1    # Move the end pointer backward

        # If the sum is greater than the target, move the end pointer backward
        elif arr[start] + arr[end] > target:
            end -= 1

        # If the sum is less than the target, move the start pointer forward
        else:
            start += 1

    # If no pairs were found, return a pair of -1, -1
    if len(ans) == 0:
        ans.append((-1, -1))

    return ans