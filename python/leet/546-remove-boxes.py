# Remove Boxes
# https://leetcode.com/problems/remove-boxes/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# DP

import functools

def removeBoxes(boxes: [int]) -> int:
    @functools.lru_cache(None)
    def dfs(i,j,k):
        if i>j: return 0
        cnt=0
        while (i+cnt)<=j and boxes[i]==boxes[i+cnt]:
            cnt+=1
        i2=i+cnt
        res=dfs(i2,j,0)+(k+cnt)**2
        for m in range(i2,j+1):
            if boxes[m]==boxes[i]:
                res=max(res, dfs(i2,m-1,0)+dfs(m,j,k+cnt))
        return res
    return dfs(0,len(boxes)-1,0)

print(removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]), 23)


# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)

# [1, 3, 2, 2, 2, 3, 4, 3, 1]

# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# 1 [0] + [3, 2, 2, 2, 3, 4, 3, 1] = 15
# 1 [1] + [1, 2, 2, 2, 3, 4, 3, 1] = 2 + 9 + 1 + 1 + 1 + 1 = 15
# 9 [2:4] + [1, 3, 3, 4, 3, 1] = 9 + 1 + 4 + 1 + 1 + 1 = 17
# 10 [1+3*3] + [3, 3, 4, 3, 1] = 17
# 9 + 4 + [1, 4, 3, 1] = 9 + 4 + 1 + 1 + 1 + 1 = 18
# 9 + 1 + [1, 3, 3, 3, 1] = 9 + 1 + 9 + = 19
# 10 + 1, [3, 3, 3, 1] = 11 + 9 + 1 = 21
# 10 + 9, [1, 1] = 10 + 9 + 4 = 23
