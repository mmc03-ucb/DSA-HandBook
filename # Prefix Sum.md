# Prefix Sum

## Overview
The prefix sum technique is a useful method for solving problems that require the calculation of sum queries over a range or subarray. By preprocessing the input array and storing the cumulative sums up to each index, we can efficiently compute range sums in **O(1)** time, after an **O(n)** preprocessing step.

### Class: `PrefixSum`

This class stores the prefix sum of the input list `nums`. The `rangeSum` method computes the sum of elements between indices `left` and `right` (inclusive) in constant time.

```python
class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
```

The `rangeSum` function works by subtracting the prefix sum at the `left-1` index from the prefix sum at the `right` index. If `left` is 0, no subtraction is needed, as the sum from the start of the array is already included.

---

## Problem: Range Sum Query - Immutable

Given an array of integers, this problem involves implementing a `sumRange` function that returns the sum of the elements between indices `left` and `right` (inclusive). The solution uses the `PrefixSum` class above.

```python
# Given an array of integers, return the sum of the elements between indices left and right (inclusive)
# O(n) preprocessing, O(1) query time
class NumArray:

    def __init__(self, nums):
        self.prefix_sum = PrefixSum(nums)

    def sumRange(self, left, right):
        return self.prefix_sum.rangeSum(left, right)
```

---