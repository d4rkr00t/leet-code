# Shortest Completing Word
# https://leetcode.com/problems/shortest-completing-word/
# easy
#
# Time:  O(n+m) where n is a length of a licensePlate and m is a length a dictionary
# Space: O(n+w) where n is a length of a licensePlate and w is a length of a word

from collections import Counter

def shortestCompletingWord(licensePlate: str, words: [str]) -> str:
    pc = Counter(filter(lambda x : x.isalpha(), licensePlate.lower()))
    return min([w for w in words if Counter(w) & pc == pc], key=len)

print(shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]), "steps")
print(shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]), "pest")
