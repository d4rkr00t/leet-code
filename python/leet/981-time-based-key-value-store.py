# Time Based Key-Value Store
# url: https://leetcode.com/problems/time-based-key-value-store/
# medium
# [1 3 4 5]


class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if (not key in self.time_map):
            self.time_map[key] = []

        self.time_map[key].append((timestamp, value))

    def get(self, key, timestamp):
        if (not key in self.time_map):
            return ""

        time_table = self.time_map[key]

        def bsearch(arr, left, right, target):  # [1 3 4 5] 0
            mid = (right + left) // 2

            if (arr[mid][0] == target):
                return arr[mid]

            if (right <= left):
                if (right < 0):
                    return ""
                if (arr[right][0] < target):
                    return arr[right]
                else:
                    return arr[right - 1]

            if (arr[mid][0] > target):
                return bsearch(time_table, left, mid - 1, timestamp)
            else:
                return bsearch(time_table, mid + 1, right, timestamp)

        pos = bsearch(time_table, 0, len(time_table) - 1, timestamp)

        print(timestamp, pos)

        return pos


kv = TimeMap()
# store the key "foo" and value "bar" along with timestamp = 1
# kv.set("foo", "bar", 1)
# print(kv.get("foo", 1))  # output "bar"
# print(kv.get("foo", 3))  # output "bar" since there is the only value is at 1
# kv.set("foo", "bar2", 4)
# print(kv.get("foo", 4))  # output "bar2"
# print(kv.get("foo", 5))  # output "bar2"

kv2 = TimeMap()
kv2.set("love", "high", 10)
kv2.set("love", "low", 20)
print(kv2.get("love", 5))
print(kv2.get("love", 10))
print(kv2.get("love", 15))
print(kv2.get("love", 20))
print(kv2.get("love", 25))

# ["TimeMap","set","get","get","set","get","get"]
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
