# UnionFind

## Overview
The **UnionFind** data structure is used to efficiently manage a partition of a set into disjoint subsets. It supports two key operations:
1. **Find**: Determines the representative or "parent" of the set containing an element.
2. **Union**: Merges two sets if they are not already connected.

To optimize these operations, we use two techniques:
1. **Path Compression** (for Find): Flattens the structure of the tree whenever `find` is called so that all nodes directly point to the root.
2. **Union by Rank/Height** (for Union): Ensures that the smaller tree is always attached under the root of the larger tree to minimize tree height.

### Time Complexity:
- **Find**: O(α(n)), where α is the inverse Ackermann function (very slow-growing), effectively making this operation almost constant time.
- **Union**: O(α(n)), similarly, this is almost constant time due to the combination of path compression and union by rank.

### Space Complexity:
- **O(n)**, where n is the number of elements, as we need space for storing parent and rank information for each element.

---

## Class Definitions

### `UnionFind`

```python
class UnionFind:
    def __init__(self, n):
        self.par = {}  # Dictionary to store the parent of each element.
        self.rank = {}  # Dictionary to store the rank (height) of each tree.

        # Initialize each element's parent to itself and rank to 0.
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find the parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            # Path compression: make each node point directly to its root.
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False  # They are already in the same set.
        
        # Union by rank: attach the smaller tree under the larger tree.
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            # If ranks are the same, arbitrarily choose one as the root and increment its rank.
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
```

---

### Key Operations

1. **Find**:
   - The `find` function returns the root or representative of the set containing element `n`. It uses **path compression** to flatten the tree structure, speeding up future `find` operations. This ensures that each node directly points to the root.
   - **Time Complexity**: O(α(n)) where α is the inverse Ackermann function.

2. **Union**:
   - The `union` function merges the sets containing two elements, `n1` and `n2`. It uses **union by rank** to ensure the smaller tree is attached to the root of the larger tree, minimizing the tree height.
   - **Time Complexity**: O(α(n)) due to the combination of path compression and union by rank.

---

### Example Usage

```python
uf = UnionFind(5)  # Create a UnionFind for 5 elements.

# Union operations
print(uf.union(1, 2))  # True (1 and 2 are not connected, so now they're connected)
print(uf.union(2, 3))  # True (2 and 3 are not connected, so now they're connected)
print(uf.union(1, 3))  # False (1 and 3 are already connected)

# Find operations
print(uf.find(1))  # 3 (1 and 3 are connected, so they have the same root)
print(uf.find(2))  # 3 (2 and 3 are connected, so they have the same root)
print(uf.find(4))  # 4 (4 is its own root)
```

---

### Summary
- The **UnionFind** structure is highly efficient for dynamically managing and merging disjoint sets. The combination of **path compression** and **union by rank** ensures that both **find** and **union** operations are almost constant time, making it ideal for problems like dynamic connectivity, Kruskal's algorithm for Minimum Spanning Tree, and cycle detection in graphs.