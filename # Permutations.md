# Permutations

## Problem: Generate All Permutations

Generate all possible permutations of a given list of numbers.

- **Time Complexity:** O(n * n!)
- **Space Complexity:** O(n * n!)

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def dp(i, perm):
            if i >= len(nums):
                perms.append(perm.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] is not None:
                    perm.append(nums[j])
                    nums[j] = None
                    dp(i+1, perm)
                    nums[j] = perm.pop()
        
        dp(0, [])
        return perms
```

## Problem: Generate Unique Permutations

Generate all unique permutations of a given list of numbers, avoiding duplicate results.

- **Time Complexity:** O(n * n!)
- **Space Complexity:** O(n * n!)

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set()

        def dp(i, perm):
            if i >= len(nums):
                perms.add(tuple(perm.copy()))
                return
            
            for j in range(len(nums)):
                if nums[j] is not None:
                    perm.append(nums[j])
                    nums[j] = None
                    dp(i+1, perm)
                    nums[j] = perm.pop()
        
        dp(0, [])
        return list(perms)
```

