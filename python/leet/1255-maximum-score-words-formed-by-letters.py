# Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections

def maxScoreWords(words: [str], letters: [str], score: [int]) -> int:
    max_score = 0
    words_score = [sum(score[ord(c)-ord('a')] for c in word) for word in words]
    words_counter = [collections.Counter(word) for word in words]

    def dfs(i, curr_score, counter):
        nonlocal max_score
        if curr_score + sum(words_score[i:]) <= max_score:
            return
        max_score = max(max_score, curr_score)
        for j, wcnt in enumerate(words_counter[i:], i):
            if all(n <= counter.get(c,0) for c,n in wcnt.items()):
                dfs(j+1, curr_score+words_score[j], {c:n-wcnt.get(c,0) for c,n in counter.items()})

    dfs(0, 0, collections.Counter(letters))
    return max_score


print(maxScoreWords(
    words = ["dog","cat","dad","good"],
    letters = ["a","a","c","d","d","d","g","o","o"],
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]), 23)

print(maxScoreWords(
    words = ["xxxz","ax","bx","cx"],
    letters = ["z","a","b","c","x","x","x"],
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]), 27)

print(maxScoreWords(
    words = ["leetcode"],
    letters = ["l","e","t","c","o","d"],
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]), 0)

# "a","a","c","d","d","d","g","o","o"
# {
#   a: 2,
#   c: 1,
#   d: 3,
#   g: 1,
#   o: 2
# }
#
# dog  5 + 2 + 3 = 10
# dad  5 + 1 + 5 = 11
# good 3 + 2 + 2 + 5 = 12
