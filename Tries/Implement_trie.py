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



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)