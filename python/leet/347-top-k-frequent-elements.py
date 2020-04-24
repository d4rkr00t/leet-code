# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# medium
#
# Time:  O(nlogk) where n is number of elements in num, and k number of uniq elements
# Space: O(n)
#
# Solution:
# Dict + Heap

import heapq
import collections

def topKFrequent(nums: [int], k: int) -> [int]:
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

print(topKFrequent(nums = [1,1,1,1,2,2,2,3,3], k = 2), [1,2])
print(topKFrequent(nums = [1], k = 1), [1])

