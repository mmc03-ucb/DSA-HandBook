# Trie Data Structure

## Overview
A **Trie** (pronounced as "try") is a tree-like data structure that stores a dynamic set of strings, where each node represents a character of a string. It is primarily used for fast searching, inserting, and prefix-based matching. Tries are especially useful for applications like autocomplete, dictionary word search, and prefix search.

### Time Complexity:
- **Insert**: O(m), where m is the length of the word being inserted.
- **Search**: O(m), where m is the length of the word being searched.
- **StartsWith**: O(m), where m is the length of the prefix.

### Space Complexity:
- **O(n * m)**, where n is the number of words and m is the average length of the words. Each word requires a node for every character, and each node has a reference to its children.

---

## Class Definitions

### `TrieNode`

Each `TrieNode` represents a single character and holds references to its children as well as a flag (`word`) that indicates whether the node marks the end of a valid word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Stores child nodes for each character.
        self.word = False    # Indicates if the node is the end of a word.
```

### `Trie`

The `Trie` class manages the root node and provides methods for inserting words, searching for words, and checking for prefixes.

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node to start the trie.
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()  # Create a new node if it doesn't exist.
            curr = curr.children[c]  # Move to the next child node.
        curr.word = True  # Mark the end of the word.

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:  # If the character isn't found, return False.
                return False
            curr = curr.children[c]  # Move to the next node.
        return curr.word  # Return True if it's the end of a valid word.

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:  # If any prefix character is missing, return False.
                return False
            curr = curr.children[c]  # Move to the next node.
        return True  # Return True if the prefix is found.
```

---

### Key Operations and Explanation

1. **Insert**:
   - Each character of the word is inserted one by one into the Trie. If a character is not already present, a new node is created. Once the last character of the word is inserted, the `word` flag is set to `True` to indicate the end of a valid word.
   - **Time Complexity**: O(m), where m is the length of the word.
   - **Space Complexity**: O(m), as new nodes may need to be created for each character in the word.

2. **Search**:
   - To check if a word exists, we traverse the Trie character by character. If a character doesn't exist in the children of the current node, the word is not present. If we reach the end of the word and the `word` flag is `True`, the word exists.
   - **Time Complexity**: O(m), where m is the length of the word.
   - **Space Complexity**: O(1), as no additional space is used except for the traversal.

3. **StartsWith**:
   - To check if any word in the Trie starts with a given prefix, we traverse the Trie character by character. If all characters of the prefix are found, it means some word in the Trie starts with that prefix.
   - **Time Complexity**: O(m), where m is the length of the prefix.
   - **Space Complexity**: O(1), as no additional space is used except for the traversal.

---
