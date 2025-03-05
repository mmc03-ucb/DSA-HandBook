# Sliding Window

## Overview
The sliding window technique is a useful approach to efficiently solve problems that involve finding a subset of elements within a given range. This method helps optimize brute-force solutions by maintaining a dynamically updating subset.

## Fixed Size Sliding Window

### Problem: Checking for Close Duplicates

Given an array, determine if there exist two duplicate values within **k** positions of each other.

```python
# Same problem using sliding window.
# O(n)
def closeDuplicates(nums, k):
    window = set()  # Current window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False
```

## Variable Size Sliding Window

### Problem: Longest Subarray with Same Values

Find the length of the longest contiguous subarray where all values are the same. This can be efficiently solved in **O(n)** time using the sliding window approach.

```python
# Find the length of longest subarray with the same 
# value in each position: O(n)
def longestSubarray(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R 
        length = max(length, R - L + 1)
    return length
```

### Problem: Shortest Subarray with Sum ≥ Target

Given an array of positive integers, find the minimum length of a contiguous subarray whose sum is greater than or equal to a given target.

```python
# Find length of the minimum size subarray where the sum is 
# greater than or equal to the target.
# Assume all values in the input are positive.
# O(n)
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length
```
---

# Two Pointers

## Overview
The two pointers technique is a powerful method for solving problems that involve iterating through a sequence from both ends or moving pointers in a specific way to optimize the solution. Usually, we start with the pointers at opposite ends (beginning and end) of the sequence and move them toward each other or adjust them based on the problem requirements.

## Problem: Checking for a Palindrome

Given a string, determine if it is a palindrome (reads the same forward and backward). This approach runs in **O(n)** time complexity.

```python
# Given a string of characters, return true if it's a palindrome,
# return false otherwise: O(n)
def isPalindrome(word):
    L, R = 0, len(word) - 1  # Start with pointers at both ends
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1  # Move the left pointer toward the center
        R -= 1  # Move the right pointer toward the center
    return True
```

## Problem: Two Sum in a Sorted Array

Given a sorted array, find two numbers that sum up to a given target. This approach runs in **O(n)** time complexity using the two-pointer technique.

```python
# Given a sorted array of integers, return the indices
# of two elements (in different positions) that sum up to
# the target value. Assume there is exactly one solution.
# O(n)
def targetSum(nums, target):
    L, R = 0, len(nums) - 1  # Start with pointers at both ends of the array
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1  # Move the right pointer leftward if the sum is too large
        elif nums[L] + nums[R] < target:
            L += 1  # Move the left pointer rightward if the sum is too small
        else:
            return [L, R]  # Return the indices when a match is found
```

## Problem: Remove Duplicates from Sorted Array

Given a sorted array, remove duplicates in place. The solution must use constant extra space and return the new length of the array.

```python
# Given a sorted array of integers, remove duplicates in place
# and return the new length of the array. The array should be modified in place.
# O(n)
def removeDuplicates(nums):
    if not nums:
        return 0
    
    L = 0  # Pointer to track the unique elements
    for R in range(1, len(nums)):  # Pointer to iterate through the array
        if nums[L] != nums[R]:
            L += 1  # Move the left pointer to the next unique position
            nums[L] = nums[R]  # Update the unique position with the current element
    
    return L + 1  # Return the length of the array without duplicates
```

## Problem: Remove Duplicates from Sorted Array II

Given a sorted array, remove duplicates such that each element appears at most twice. The solution should use constant extra space and return the new length of the array.

```python
# Given a sorted array of integers, remove duplicates such that each element appears
# at most twice and return the new length of the array. The array should be modified in place.
# O(n)
def removeDuplicatesII(nums):
    if not nums:
        return 0
    
    L = 1  # Pointer to track the valid position for duplicates
    count = 1  # To count the occurrences of each number
    
    for R in range(2, len(nums)):  # Pointer to iterate through the array
        if nums[R] == nums[R - 1]:
            count += 1
        else:
            count = 1
        
        if count <= 2:
            nums[L] = nums[R]  # Move the left pointer to the next valid position
            L += 1  # Increment the left pointer only when a valid number is found
    
    return L  # Return the length of the array with the allowed duplicates
```