# Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/
# medium
#
# Time:  O(log n)
# Space: O(1)
#
# Solution:
# Binary Search + Two Pointers

def findClosestElements(arr: [int], k: int, x: int) -> [int]:
    def find_x_pos(arr, x, start, end):
        if start >= end:
            return min(max(end, 0), len(arr) - 1)

        mid = (end + start) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            return find_x_pos(arr, x, mid + 1, end)
        else:
            return find_x_pos(arr, x, start, mid-1)


    index = find_x_pos(arr, x, 0, len(arr) - 1)
    low = max(0, index - k - 1)
    high = min(len(arr) - 1, index + k - 1)

    while high - low > k - 1:
        if low < 0 or x - arr[low] <= arr[high] - x:
            high -= 1
        else:
            low += 1

    return arr[low:high+1]

print(findClosestElements([1,2,3,4,5], k=4, x=3), [1,2,3,4])
print(findClosestElements([1,2,3,4,5], k=4, x=-1), [1,2,3,4])
print(findClosestElements([1,2,3,4,5], k=2, x=6), [4,5])
print(findClosestElements([1,2,4,5], k=2, x=3), [2,4])
print(findClosestElements([1,2,4,5,6,7,8,9,10], k=8, x=2), [1,2,4,5,6,7,8,9])
