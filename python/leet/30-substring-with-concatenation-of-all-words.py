# Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# hard
import collections


def build_dict(words):
    d = {}
    for w in words:
        d[w] = d[w] + 1 if w in d else 1

    return d


def findSubstring(s, words):  # "barfoothefoobarman", ["foo", "bar"]
    if not s or not words:
        return []

    step = len(words[0])  # 3

    if len(s) < step:
        return []

    d = build_dict(words)  # { foo: 1, bar: 1 }
    res = []

    for start in range(0, len(s)):
        total = 0
        matches = collections.defaultdict(int)
        for end in range(start, len(s) + 1, step):
            word = s[end:(end+step)]

            if word in d:
                matches[word] += 1
                total += 1

                if matches[word] > d[word]:
                    break

                if total == len(words):
                    res.append(start)
                    break

            else:
                break

    return res  # [0, 9]


print(findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9])
print(findSubstring("wordgoodgoodgoodbestword",
                    ["word", "good", "best", "word"]), [])
print(findSubstring("barfoofoobarthefoobarman",
                    ["bar", "foo", "the"]), [6, 9, 12])
print(findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                    ["fooo", "barr", "wing", "ding", "wing"]), [13])
