# Subsets

## Time Complexity:
- Both approaches (without and with duplicates) have **O(n * 2^n)** time complexity because in the worst case, there are **2^n** subsets, and for each subset, the algorithm does an operation that takes **O(n)** time to copy the subset.
  
## Space Complexity:
- Both approaches have **O(n)** space complexity for storing the current subset during recursion. The total space also accounts for storing the subsets in the result.

---

## Functions Overview

### 1. `subsetsWithoutDuplicates`

This function generates all possible subsets from a list of integers, where the list doesn't contain duplicate elements.

#### Algorithm:
- The function uses backtracking to explore every possible inclusion or exclusion of elements in the subset.
- At each step, it makes a decision to either include or exclude the current element and recursively processes the rest of the list.
- Once it reaches the end of the list, it appends the current subset to the result list.

#### Code:
```python
def subsetsWithoutDuplicates(nums):
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets

def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    # decision NOT to include nums[i]
    helper(i + 1, nums, curSet, subsets)
```

#### Time and Space Complexity:
- **Time Complexity**: O(n * 2^n), where n is the number of elements. In the worst case, the algorithm explores all subsets, and each subset operation takes O(n) to copy.
- **Space Complexity**: O(n), where n is the number of elements. This accounts for the current subset (`curSet`) being tracked during recursion.

---

### 2. `subsetsWithDuplicates`

This function generates all possible subsets from a list of integers, but the input list may contain duplicates. It ensures that duplicates are not included in the result.

#### Algorithm:
- The function first sorts the input list to ensure that duplicates are adjacent.
- It uses backtracking similar to the previous function, but it skips over duplicates when making decisions not to include an element. This prevents generating duplicate subsets.
  
#### Code:
```python
def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper2(0, nums, curSet, subsets)
    return subsets

def helper2(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return
    
    # decision to include nums[i]
    curSet.append(nums[i])
    helper2(i + 1, nums, curSet, subsets)
    curSet.pop()

    # decision NOT to include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, curSet, subsets)
```

#### Time and Space Complexity:
- **Time Complexity**: O(n * 2^n), where n is the number of elements. Similar to the previous function, but here we also handle skipping duplicates.
- **Space Complexity**: O(n), where n is the number of elements. The current subset (`curSet`) takes up O(n) space, and we track all subsets in the result.

---

### Example Usage

#### 1. Without Duplicates:
```python
nums = [1, 2, 3]
print(subsetsWithoutDuplicates(nums))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

#### 2. With Duplicates:
```python
nums = [1, 2, 2]
print(subsetsWithDuplicates(nums))
# Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

---

### Summary
- **Backtracking** is used to generate all possible subsets. For the function handling duplicates, we sort the input to group duplicates together and skip the duplicate paths during recursion.
- Both methods generate all subsets, but the second method ensures no duplicate subsets are included in the result by skipping duplicate choices.