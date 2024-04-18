## Trie Implementation

### Intuition
The problem requires implementing a Trie data structure and providing methods for inserting a word into the Trie, searching for a word, and checking if a word starts with a given prefix.

### Approach
We define a `TrieNode` class representing a single node in the Trie. Each `TrieNode` contains a dictionary `child` to store child nodes and a boolean `is_end_of_word` flag indicating if the node represents the end of a word.

The `Trie` class initializes with a root `TrieNode`. The `insert` method iterates through each character of the word, creating new `TrieNodes` if necessary and marking the end of the word by setting the `is_end_of_word` flag to True.

The `search` method traverses the Trie to check if the word exists. It returns True only if the word exists in the Trie.

The `startsWith` method checks if there is any word in the Trie that starts with the given prefix. It returns True if the prefix is found in the Trie.

### TrieNode Class:
- **Purpose**: Represents a single node in the Trie data structure.
- **Attributes**:
  - `child`: A dictionary that maps characters to TrieNode objects. It stores the child nodes of the current node, representing the possible next characters in the trie.
  - `is_end_of_word`: A boolean flag indicating whether the node represents the end of a word. It's set to `True` if the node represents the end of a word, otherwise `False`.

### Trie Class:
- **Purpose**: Implements the Trie data structure and provides methods for inserting, searching, and checking prefixes.
- **Constructor (`__init__`)**:
  - Initializes a Trie object with a root node of type TrieNode.

- **insert Method**:
  - **Parameters**: `word` (str) - The word to be inserted into the Trie.
  - **Functionality**:
    - Traverses the Trie while iterating through each character of the `word`.
    - For each character, checks if it exists in the current node's `child` dictionary.
    - If the character doesn't exist in the `child` dictionary, creates a new TrieNode and adds it to the dictionary.
    - Moves the `node` pointer to the child node corresponding to the current character.
    - Once the entire word is inserted, sets the `is_end_of_word` flag of the last node to `True` to mark the end of the word.

- **search Method**:
  - **Parameters**: `word` (str) - The word to be searched in the Trie.
  - **Functionality**:
    - Traverses the Trie while iterating through each character of the `word`.
    - Checks if each character exists in the current node's `child` dictionary.
    - If any character is missing, returns `False`, indicating that the word doesn't exist in the Trie.
    - Once the entire word is traversed, returns the value of the `is_end_of_word` flag of the last node. If it's `True`, the word exists in the Trie; otherwise, it doesn't.

- **startsWith Method**:
  - **Parameters**: `prefix` (str) - The prefix to be checked in the Trie.
  - **Functionality**:
    - Traverses the Trie while iterating through each character of the `prefix`.
    - Checks if each character exists in the current node's `child` dictionary.
    - If any character is missing, returns `False`, indicating that the prefix doesn't exist in the Trie.
    - If the entire prefix is found in the Trie, returns `True`.

### Example Usage:
- Instantiate a Trie object: `obj = Trie()`
- Insert a word into the Trie: `obj.insert(word)`
- Search for a word in the Trie: `param_2 = obj.search(word)`
- Check if a prefix exists in the Trie: `param_3 = obj.startsWith(prefix)`

### Complexity
- Time complexity:
  - Insertion: O(m), where m is the length of the word.
  - Search and startsWith: O(m), where m is the length of the word or prefix being searched.
- Space complexity: O(n*m), where n is the number of words inserted into the Trie and m is the average length of the words.

### Code
```python
class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()  # Create a new Trie node if the character doesn't exist
            node = node.child[char]
        node.is_end_of_word = True  # Mark the end of the inserted word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.child:
                return False  # If any character is missing, the word doesn't exist
            node = node.child[char]
        return node.is_end_of_word  # Return True only if the word exists in the Trie

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False  # If any character in the prefix is missing, return False
            node = node.child[char]
        return True  # Return True if the prefix is found in the Trie
