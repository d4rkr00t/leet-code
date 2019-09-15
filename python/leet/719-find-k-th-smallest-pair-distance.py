# Find K-th Smallest Pair Distance
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# hard


def smallestDistancePair(nums, k):
    def possible(guess):
        # Is there k or more pairs with distance <= guess?
        count = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > guess:
                left += 1
            count += right - left
        return count >= k

    nums.sort()
    lo = 0
    hi = nums[-1] - nums[0]
    while lo < hi:
        mi = (lo + hi) / 2
        if possible(mi):
            hi = mi
        else:
            lo = mi + 1

    return int(lo)


print(smallestDistancePair([1, 9, 10, 8, 7, 5, 4, 6, 3, 2], 40), 2)
print(smallestDistancePair([62, 4, 100], 2), 58)
