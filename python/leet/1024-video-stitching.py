# Video Stitching
# https://leetcode.com/problems/video-stitching/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# 1. Sort by start time
# 2. Then DP
# if prev interval covers
# if dp[i-1][j] != None:
#    dp[i][j] = dp[i-1][j]
#
# if prev doesn't cover and current coverrs
# if dp[i-1][j] == None:
#    dp[i][j] = dp[i][clip[0]] + 1
#
# if prev doesn't cover and cur doesn't
#    dp[i][j] = None


def videoStitching(clips: [[int]], T: int) -> int:
    # 1. Sort by start time
    clips = sorted(clips, key = lambda item: item[0])

    if not clips or clips[0][0] != 0:
        return -1

    # 2. Build a DP table
    dp = [[None] * (T + 1) for x in range(len(clips) + 1)]
    dp[0][0] = 0

    for i in range(1, len(clips) + 1):
        dp[i][0] = 1

    # 3. Calculate DP solutions
    for i in range(1, len(clips) + 1):
        clip = clips[i-1]
        for j in range (1, T + 1):
            # if prev covers cur region
            if dp[i-1][j] != None:
                dp[i][j] = dp[i-1][j]

            # if doesn't cover region but cur does
            elif clip[0] <= j and clip[1] >= j:
                if clip[0] == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][clip[0]] + 1 if dp[i-1][clip[0]] != None else None

            # if doesn't cover region and cur doesn't
            elif clip[0] > j or clip[1] < j:
                dp[i][j] = None

    return dp[-1][-1] if dp[-1][-1] != None else -1

print(videoStitching(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10), 3)
print(videoStitching(clips = [[0,1],[1,2]], T = 5), -1)
print(videoStitching(clips = [[0,4],[2,8]], T = 5), 2)
print(videoStitching(clips = [[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]], T = 5), 1)
