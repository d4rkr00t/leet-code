# Student Attendance Record II
# https://leetcode.com/problems/student-attendance-record-ii/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# – DP

def checkRecord(n: int) -> int:
    m = 1000000007
    if n == 1:
        return 3

    if n == 0:
        return 0

    nums = [1, 1, 2]
    i = 2

    while i < n:
        nums.append((nums[i] + nums[i-1] + nums[i-2]) % m)
        i += 1

    result = (nums[n] + nums[n-1] + nums[n-2]) % m

    for i in range(n):
        result += nums[i+1] * nums[n-i] % m
        result %= m

    return result

print(checkRecord(2), 8)
print(checkRecord(3), 19)
print(checkRecord(4), 43)
print(checkRecord(5), 94)
print(checkRecord(6), 200)
print(checkRecord(10), 3536)
print(checkRecord(20), 2947811)
