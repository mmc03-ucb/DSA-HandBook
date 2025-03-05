# Kadane's Algorithm

## Overview

Kadane's Algorithm is an efficient method to find the maximum sum of a contiguous subarray in a given array of integers. It operates in **O(n)** time complexity using dynamic programming principles.

## Implementation

### Basic Kadane's Algorithm

This function calculates the maximum subarray sum.

```python
# Kadane's Algorithm: O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum
```

### Sliding Window Variation

This variation returns the left and right indices of the maximum subarray sum.

```python
# Sliding window variation of Kadane's: O(n)
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]
```

### Circular Subarray Variation

This variation handles cases where the subarray can wrap around the end of the array.

```python
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        maxSum = nums[0]

        totalMax = 0
        totalMin = 0
        total = 0
        for n in nums:
            totalMax = max(totalMax, 0)
            totalMax += n
            maxSum = max(maxSum, totalMax)

            totalMin += n
            totalMin = min(totalMin, n)
            minSum = min(totalMin, minSum)

            total += n
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
```

## Example Walkthrough

Consider the input array:

```python
nums = [4, -1, 2, -7, 3, 4]
```

We initialize `curSum = 0` and `maxSum = 4` (the first element). As we iterate:

1. Add `4` → `curSum = 4`, `maxSum = 4`
2. Add `-1` → `curSum = 3`, `maxSum = 4`
3. Add `2` → `curSum = 5`, `maxSum = 5`
4. Add `-7` → `curSum = -2`, `maxSum = 5` (reset `curSum` to `0` as it's negative)
5. Add `3` → `curSum = 3`, `maxSum = 5`
6. Add `4` → `curSum = 7`, `maxSum = 7`

Thus, the maximum subarray sum is **7**, from index **4 to 5** (`[3, 4]`).

```python
print(kadanes(nums))  # Output: 7 (subarray: [3, 4])
print(slidingWindow(nums))  # Output: [4, 5] (indices of subarray [3, 4])
```

