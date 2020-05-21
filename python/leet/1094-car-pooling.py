# Car Pooling
# https://leetcode.com/problems/car-pooling/
# medium
#
# Time:  O(n)
# Space: O(m)
#
# Solution:
# TBD

def carPooling(trips: [[int]], capacity: int) -> bool:
    loc = [0] * 1001

    for n,s,e in trips:
        loc[s] += n
        loc[e] -= n

    num_pas = 0

    for n in loc:
        num_pas += n
        if num_pas > capacity:
            return False

    return True

print(carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4), False)
print(carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5), True)
print(carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3), True)
print(carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11), True)
