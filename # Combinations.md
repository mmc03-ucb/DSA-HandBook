# Combinations

## Time Complexity:
1. **`combinations`**: O(k * 2^n), where `k` is the size of the combination and `n` is the number of available numbers. The worst case occurs when generating all possible combinations of size `k` from `n` elements. The algorithm explores subsets using backtracking, and for each element, it either includes it or skips it.
2. **`combinations2`**: O(k * C(n, k)), where C(n, k) is the number of combinations (n choose k). The runtime is dependent on the number of combinations to be generated, which is the binomial coefficient, and the length of each combination is `k`.

## Space Complexity:
- **O(k)** for both methods because we're storing combinations of size `k` and maintaining the current combination as we explore different possibilities.

---

## Functions Overview

### 1. `combinations`

This function generates all combinations of size `k` from a range of numbers from 1 to `n` using **backtracking**.

#### Algorithm:
- The function starts by calling the helper function to explore combinations.
- It explores two choices at each step: including or excluding the current element `i` in the combination.
- It continues recursively and, when the combination reaches the desired size `k`, it adds it to the result.

#### Code:
```python
def combinations(n, k):
    combs = []
    helper(1, [], combs, n, k)
    return combs

def helper(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    # decision to include i
    curComb.append(i)
    helper(i + 1, curComb, combs, n, k)
    curComb.pop()
    
    # decision to NOT include i
    helper(i + 1, curComb, combs, n, k)
```

#### Time and Space Complexity:
- **Time Complexity**: O(k * 2^n), because we explore subsets and generate combinations of size `k`.
- **Space Complexity**: O(k), as we're storing the current combination of size `k` during the recursion.

---

### 2. `combinations2`

This function also generates all combinations of size `k` from a range of numbers from 1 to `n`, but it uses a different approach, where it directly generates the combinations without backtracking.

#### Algorithm:
- It uses a for loop inside the recursive helper function, iterating from the current index `i` to `n`. This ensures that combinations are built in lexicographical order without having to backtrack.
- The helper function directly appends elements to the current combination and recurses to generate further combinations.

#### Code:
```python
def combinations2(n, k):
    combs = []
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        combs.append(curComb.copy())
        return
    if i > n:
        return
    
    for j in range(i, n + 1):
        curComb.append(j)
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop()
```

#### Time and Space Complexity:
- **Time Complexity**: O(k * C(n, k)), where C(n, k) is the number of combinations of size `k` from `n` elements.
- **Space Complexity**: O(k), as we're storing the current combination of size `k`.

---

### Example Usage

#### 1. `combinations`
```python
n = 4
k = 2
print(combinations(n, k))
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

#### 2. `combinations2`
```python
n = 4
k = 2
print(combinations2(n, k))
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

---

### Summary
- Both functions generate **combinations of size k** from a range of `1` to `n`, but they use different techniques:
  1. **Backtracking (in `combinations`)**: Explores both including and excluding each element.
  2. **Iterative construction (in `combinations2`)**: Directly generates combinations using a for loop and recursion.
- **Time complexity** for both approaches is exponential in nature, but the second method (`combinations2`) is more efficient in terms of avoiding unnecessary backtracking.