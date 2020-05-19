# Split Array into Fibonacci Sequence
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Backtracking

def splitIntoFibonacci(S: str) -> [int]:
    for i in xrange(min(10, len(S))):
        x = S[:i+1]
        if x != '0' and x.startswith('0'): break
        a = int(x)
        for j in xrange(i+1, min(i+10, len(S))):
            y = S[i+1: j+1]
            if y != '0' and y.startswith('0'): break
            b = int(y)
            fib = [a, b]
            k = j + 1
            while k < len(S):
                nxt = fib[-1] + fib[-2]
                nxtS = str(nxt)
                if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                    k += len(nxtS)
                    fib.append(nxt)
                else:
                    break
            else:
                if len(fib) >= 3:
                    return fib
    return []

print(splitIntoFibonacci("123456579"), [123, 456, 579])
print(splitIntoFibonacci("11235813"), [1,1,2,3,5,8,13])
print(splitIntoFibonacci("112358130"), [])
print(splitIntoFibonacci("1101111"), [110, 1, 111])
print(splitIntoFibonacci("0000"), [0,0,0,0])
# ----
print(splitIntoFibonacci("0123"), [])
print(splitIntoFibonacci(""), [])
print(splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))

# 11235813
# nums: [] | [1] | [1, 1] | [1,1,2] | [1,1,2,3] | [1,1,2,3,5] | [1,1,2,3,5,8] | [1,1,2,3,5,8,13]
# pos:  0  |   1 |  2     | 3       | 4         | 5           | 6             | 8
# size: 1  |   1 |  1     | 1       | 1         | 1           | 2             | 2
#
#
# 1101111
# nums: [] | [1] | [1, 1] | [1, 1, 0]
# pos:  0  |   1 |   2    |   3
# size: 1  |   1 |   1    |   1

# [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
