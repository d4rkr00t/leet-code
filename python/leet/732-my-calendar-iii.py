# My Calendar III
# https://leetcode.com/problems/my-calendar-iii/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

class MyCalendarThree:

    def __init__(self):
        self.K = 1
        self.bookings = None


    def book(self, start: int, end: int) -> int:
        booking = { "start": start, "end": end, "high": end, "left": None, "right": None }
        if not self.bookings:
            self.bookings = booking
            return self.K

        self.__book__(self.bookings, booking)
        self.__K__(self.bookings, booking, 1)

        return self.K

    def __is_overlapping_(self, s1, e1, s2, e2):
        # 1 ___     ___   ___   _
        # 2  ___   ___     _   ___
        return s1 < e2 and e1 > s2

    def __K__(self, parent, booking, K):
        if not parent:
            return

        if parent != booking and self.__is_overlapping_(parent["start"], parent["end"], booking["start"], booking["end"]):
            K += 1
            self.K = max(self.K, K)

        if parent["high"] < booking["start"]:
            return

        if parent["start"] < booking["start"] or parent["start"] < booking["end"]:
            self.__K__(parent["right"], booking, K)

        self.__K__(parent["left"], booking, K)


    def __book__(self, parent, booking):
        if not parent:
            return booking

        parent["high"] = max(parent["high"], booking["end"])
        if parent["start"] < booking["start"]:
            parent["right"] = self.__book__(parent["right"], booking)
        else:
            parent["left"] = self.__book__(parent["left"], booking)

        return parent


cal = MyCalendarThree()

print(cal.book(10, 20)) # returns 1
print(cal.book(50, 60)) # returns 1
print(cal.book(10, 40)) # returns 2
print(cal.book(5, 15)) # returns 3
print(cal.book(5, 60)) # returns 3
print(cal.book(25, 55)) # returns 3
