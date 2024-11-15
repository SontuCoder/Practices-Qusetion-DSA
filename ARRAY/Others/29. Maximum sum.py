# Given an array, find the maximum sum of a
# subsequence with the constraint that no 2 numbers in
# the sequence should be adjacent in the array.

# Input: arr[] = {5, 5, 10, 100, 10, 5}
# Output: 110
# Input: arr[] = {1, 2, 3}
# Output: 4
# Input: arr[] = {1, 20, 3}
# Output: 20

def max_sum_non_adjacent(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    
    prev1 = max(arr[0], arr[1])
    prev2 = arr[0]

    for i in range(2, n):
        current = max(arr[i] + prev2, prev1)
        prev2 = prev1
        prev1 = current

    return prev1

# Example usage
arr = [3, 2, 5, 10, 7]
print("Maximum sum of non-adjacent elements:", max_sum_non_adjacent(arr))