# Minimum Number of Refueling Stops
# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Heap, Dynamic Programming

import heapq

def minRefuelStops(target: int, startFuel: int, stations: [[int]]) -> int:
    pq = []  # A maxheap is simulated using negative values
    stations.append((target, float('inf')))

    ans = prev = 0
    for location, capacity in stations:
        startFuel -= location - prev
        while pq and startFuel < 0:  # must refuel in past
            startFuel += -heapq.heappop(pq)
            ans += 1
        if startFuel < 0: return -1
        heapq.heappush(pq, -capacity)
        prev = location

    return ans


print(minRefuelStops(target = 1, startFuel = 1, stations = []), 0)
print(minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]), -1)
print(minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]), 2)
print(minRefuelStops(target = 120, startFuel = 10, stations = [[10,100],[20,10],[30,30],[60,40]]), 2)
print(minRefuelStops(target = 100, startFuel = 50, stations = [[25,25],[50,50]]), 1)
