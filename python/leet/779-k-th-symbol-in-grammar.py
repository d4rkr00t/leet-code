# K-th Symbol in Grammar
# https://leetcode.com/problems/k-th-symbol-in-grammar/
# medium

def kthGrammar(N: int, K: int) -> int:
    return bin(K - 1).count('1') & 1

print(kthGrammar(1, 1), 0)
print(kthGrammar(2, 1), 0)
print(kthGrammar(2, 2), 1)
print(kthGrammar(4, 5), 1)
print(kthGrammar(4, 6), 0)
print(kthGrammar(4, 7), 0)
print(kthGrammar(4, 8), 1)
