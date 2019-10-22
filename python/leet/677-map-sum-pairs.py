# Map Sum Pairs
# https://leetcode.com/problems/map-sum-pairs/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Trie


class TrieNode(object):
    __slots__ = 'children', 'score'

    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


obj = MapSum()
# obj.insert(key, val)
# param_2 = obj.sum(prefix)

# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
