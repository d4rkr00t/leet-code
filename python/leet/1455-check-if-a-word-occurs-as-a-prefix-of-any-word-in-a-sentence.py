# Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# easy
#
# Time:  O(n+m)
# Space: O(n)


def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    for i, w in enumerate(sentence.split(' ')):
        if w.find(searchWord) == 0:
            return i

    return -1
