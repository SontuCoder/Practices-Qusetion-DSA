# 209. Minimum Size Subarray Sum

def minimum_size(arr, target):
    rear = 0
    current_sum = 0
    min_size = float('inf')  # Initialize to infinity for minimum comparison

    for front in range(len(arr)):
        current_sum += arr[front]  # Expand the window by adding arr[front]

        # Shrink the window from the left as long as the sum is greater than or equal to target
        while current_sum >= target:
            min_size = min(min_size, front - rear + 1)
            current_sum -= arr[rear]
            rear += 1

    # If min_size was not updated, it means no valid subarray was found
    return min_size if min_size != float('inf') else 0

arr = [1,2,3,4,5]
target = 11
print(minimum_size(arr,target))