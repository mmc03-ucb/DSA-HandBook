# Linked List with Two Pointers

## Overview
Using two pointers (often referred to as **slow** and **fast** pointers) is a common technique in linked list problems. It allows for efficient traversal and manipulation of the list with minimal space complexity (i.e., **O(1)** space). The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. This technique is particularly useful for problems like finding the middle of the list or detecting cycles.

---

## Problem: Find the Middle of a Linked List

This problem requires finding the middle node of a linked list. The slow pointer moves one step at a time, and the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

```python
# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Explanation:
- `slow` pointer moves one step at a time.
- `fast` pointer moves two steps at a time.
- When `fast` reaches the end, `slow` will be at the middle of the list.

---

## Problem: Determine if the Linked List Contains a Cycle

This problem determines if the linked list has a cycle (i.e., whether a node points back to a previous node in the list). If the `slow` and `fast` pointers meet, there is a cycle; otherwise, the list does not have a cycle.

```python
# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Explanation:
- Both `slow` and `fast` start at the head of the list.
- `slow` moves one step at a time, while `fast` moves two steps at a time.
- If the list has a cycle, the `slow` and `fast` pointers will eventually meet at the same node.

---

## Problem: Find the Start of the Cycle in a Linked List

This problem builds upon the cycle detection technique to not only detect if a cycle exists but also to return the node where the cycle begins.

```python
# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
```

### Explanation:
1. **Cycle Detection**: The first part of the function uses the slow and fast pointers to detect if there is a cycle.
2. **Finding the Cycle Start**: If a cycle is detected, a second pointer (`slow2`) is introduced, which starts at the head. Both pointers (`slow` and `slow2`) then move one step at a time until they meet at the start of the cycle.
   
---

These problems are classic examples of how two-pointer techniques can be used to efficiently solve linked list-related problems, with time complexity of **O(n)** and space complexity of **O(1)**.