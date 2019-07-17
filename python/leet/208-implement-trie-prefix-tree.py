# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# medium


class Node:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def get_char_pos(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pos = 0
        node = self.root

        while pos < len(word):
            ch = word[pos]
            ch_pos = self.get_char_pos(ch)

            if node.children[ch_pos]:
                node = node.children[ch_pos]
            else:
                node.children[ch_pos] = Node()
                node = node.children[ch_pos]

            pos += 1

        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        pos = 0
        node = self.root

        while pos < len(word):
            ch = word[pos]
            ch_pos = self.get_char_pos(ch)

            if not node.children[ch_pos]:
                return False

            node = node.children[ch_pos]
            pos += 1

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        pos = 0
        node = self.root

        while pos < len(prefix):
            ch = prefix[pos]
            ch_pos = self.get_char_pos(ch)

            if not node.children[ch_pos]:
                return False

            node = node.children[ch_pos]
            pos += 1

        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"), True)
print(trie.search("app"), False)
print(trie.startsWith("app"), True)
trie.insert("app")
print(trie.search("app"), True)
