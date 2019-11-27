# My Calendar II
# https://leetcode.com/problems/my-calendar-ii/
# medium
#
# Time:  O(n^2) - n number of intervals
# Space: O(n) - n number of intervals

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:

        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))

        return True


a = MyCalendarTwo()

print(a.book(10,20), True)
print(a.book(50,60), True)
print(a.book(10,40), True)
print(a.book(5,15), False)
print(a.book(5,10), True)
print(a.book(25,55), True)

#
#       |----|   |-----|
#           |------|
#         |---|


#     10         20
#      |----------|
#      |--------------------|
# |----------|
# |----|
