Python Gotcha: `list * n` Creates Shared References

### ❗ The Problem:
Using multiplication to create a list of lists can lead to **unexpected behavior** due to **shared references**.

```python
count = [[]] * 5
```

This creates a list where **each element points to the same list object**:

```python
>>> count[0].append(1)
>>> print(count)
[[1], [1], [1], [1], [1]]
```

All sublists are modified because they reference the **same** list in memory.

---

### ✅ The Solution:
Use a list comprehension to create **independent sublists**:

```python
count = [[] for _ in range(5)]
```

Now each sublist is a separate object:

```python
>>> count[0].append(1)
>>> print(count)
[[1], [], [], [], []]
```

---