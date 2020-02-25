# RLE Iterator
# https://leetcode.com/problems/rle-iterator/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# TBD

class RLEIterator:

    def __init__(self, A: [int]):
        self.seq = A # [0,8,0,9,2,5]
        self.pos = 0 # 4

    def next(self, n: int) -> int: # 1
        if not self.seq or self.pos >= len(self.seq):
            return -1

        cur = self.seq[self.pos] # 2
        while cur < n: # False
            self.seq[self.pos] = 0
            n = n - cur # 1

            if self.pos + 2 < len(self.seq):
                self.pos += 2
                cur = self.seq[self.pos]
            else:
                return -1

        self.seq[self.pos] -= n; # 2 - 1 = 1
        item = self.seq[self.pos + 1] # 5

        if self.seq[self.pos] == 0:
            self.pos += 2

        return item

obj = RLEIterator([3,8,0,9,2,5])
print(obj.next(2), 8)
print(obj.next(1), 8)
print(obj.next(1), 5)
print(obj.next(2), -1)
