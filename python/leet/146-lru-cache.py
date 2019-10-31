# LRU Cache
# https://leetcode.com/problems/lru-cache/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__lru = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__lru:
            self.__lru.move_to_end(key)
            return self.__lru[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.__lru[key] = value
        self.__lru.move_to_end(key)

        if len(self.__lru.keys()) > self.__capacity:
            self.__lru.popitem(0)


lru = LRUCache(10)
