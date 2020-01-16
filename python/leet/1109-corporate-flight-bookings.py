# Corporate Flight Bookings
# https://leetcode.com/problems/corporate-flight-bookings/
# medium
#
# Time:  O(bookings)
# Space: O(n)
#
# Solution:
# Running total / cumulative sum


def corpFlightBookings(bookings: [[int]], n: int) -> [int]:
    total = [0] * (n + 1)

    for b in bookings:
        total[b[0]-1] += b[2]
        total[b[1]] -= b[2]

    tmp = 0
    for i in range(n):
        tmp += total[i]
        total[i] = tmp

    return total[:n]


print(corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5), [10,55,45,25,25])

