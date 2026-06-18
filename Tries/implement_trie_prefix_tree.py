# Problem: Implement Trie (Prefix Tree)
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# A Trie stores words character by character.
#
# Each node contains:
# - children: maps characters to child nodes.
# - is_word: indicates whether a complete word ends here.
#
# Operations:
# insert(word)      -> Add a word.
# search(word)      -> Check if the complete word exists.
# startsWith(prefix)-> Check if any word starts with the prefix.

# Time Complexity:
# insert()      -> O(n)
# search()      -> O(n)
# startsWith()  -> O(n)
#
# n = length of the word/prefix.

# Space Complexity:
# O(total characters inserted)

# Common Mistake:
# Returning True after traversing all characters in search().
# You must also verify that the last node marks
# the end of a complete word using is_word.

# Revision Note:
# Trie Node:
# children -> next characters
# is_word  -> marks end of a valid word

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_word = True

    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_word

    def startsWith(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return False

            node = node.children[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)