# Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Stack

def largestRectangleArea(heights: [int]) -> int:
    heights.append(0)

    stack = [-1]
    rect = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            rect = max(rect, h * w)

        stack.append(i)
    return rect


print(largestRectangleArea([2,1,5,6,2,3,3,2]), 12)
print(largestRectangleArea([2,1,5,6,2,3]), 10)
print(largestRectangleArea([5,4,1,2]), 8)
print(largestRectangleArea([3,6,5,7,4,8,1,0]), 20)
