# Distance Between Bus Stops
# https://leetcode.com/problems/distance-between-bus-stops/
# easy
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def distanceBetweenBusStops(distance: [int], start: int, destination: int) -> int:
    total_dist = sum(distance)
    s = min(start, destination)
    d = max(start, destination)
    clockwise = 0

    for i in range(s, d):
        clockwise += distance[i]

    return clockwise if clockwise <= total_dist / 2 else total_dist - clockwise

print(distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1), 1)
print(distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3), 4)
