# Generate Random Point in a Circle
# https://leetcode.com/problems/generate-random-point-in-a-circle/
# medium
#
# Time:  O(1)
# Space: O(1)
#
# Solution:
# Math

import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def __isinside__(self, x, y):
        return pow((x-self.x_center), 2) + pow((y-self.y_center), 2) <= pow(self.radius, 2)

    def __get_random__(self):
        x_lower = self.x_center - self.radius
        x_upper = self.x_center + self.radius

        y_lower = self.y_center - self.radius
        y_upper = self.y_center + self.radius

        return [random.uniform(x_lower, x_upper), random.uniform(y_lower, y_upper)]

    def randPoint(self) -> [float]:
        point = self.__get_random__()

        while not self.__isinside__(point[0], point[1]):
            point = self.__get_random__()

        return point


s = Solution(1, 0, 0)
print(s.randPoint())
print(s.randPoint())
print(s.randPoint())


