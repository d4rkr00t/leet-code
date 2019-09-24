# Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# medium
#
# Time:  O(max(n, m)), where n,m respective sizes of version strings
# Space: O(n+m)
#
# Solution:
# 1. Split strings by .
# 2. Convert each section to a number
# 3. Compare left to right if beyond range assume 0


def compareVersion(version1: str, version2: str) -> int:
    if not version1 and not version2:
        return 0
    if not version1:
        return -1
    if not version2:
        return 1

    v1 = version1.split('.')
    v2 = version2.split('.')
    counter = 0
    max_len = max(len(v1), len(v2))

    while counter < max_len:
        version_number1 = int(v1[counter]) if len(v1) > counter else 0
        version_number2 = int(v2[counter]) if len(v2) > counter else 0

        if version_number1 > version_number2:
            return 1
        elif version_number2 > version_number1:
            return -1

        counter += 1

    return 0


print(compareVersion("7.5.002.4", "7.5.3"))
