"""
Kadane's Algorithm
Maximum subarray sum of a contiguous subarray in an array
"""


def kadanes(arr):
    maxSum = arr[0]

    total = 0
    for num in arr:
        total = max(total, 0)
        total += num

        maxSum = max(total, maxSum)

    return maxSum


print(kadanes([4, -1, 2, -7, 3, 4]))
