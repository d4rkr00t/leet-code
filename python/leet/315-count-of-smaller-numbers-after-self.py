# Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# hard
#
# Time:  O(n*logn)
# Space: O(n)
#
# Solution:
# BST

def countSmaller(nums: [int]) -> [int]:
    def sort(enum):
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))

    return smaller

# print(countSmaller([5]), [0])
# print(countSmaller([5,2,6,1]), [2,1,1,0])
# print(countSmaller([5,6,7,8,9,1,1,1,1,1,1]), [6,6,6,6,6,0,0,0,0,0,0])
print(countSmaller([26, 78,27,100,33,67,90,23,66,5,38]), [2, 7, 2, 7, 2, 4, 4, 1, 2, 0, 0])
# print(countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]), [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0])
