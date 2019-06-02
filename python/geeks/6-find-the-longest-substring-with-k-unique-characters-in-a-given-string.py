# Find the longest substring with k unique characters in a given string
# url: https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


def find_longest(s, k):
    if (len(s) == 0):
        return "Error"

    stack = [0]
    cur_char = s[0]
    cur_pos = 1
    ans = ""

    while (cur_pos <= len(s)):
        if (cur_pos == len(s) or cur_char != s[cur_pos]):
            stack.append(cur_pos)

            if (cur_pos < len(s)):
                cur_char = s[cur_pos]

        start = len(stack) - 1 - k

        if (start >= 0):
            size = stack[-1] - stack[start]

            if (size > len(ans)):
                ans = s[start:start+size]

        cur_pos += 1

    if (len(ans) == 0):
        return "Error"

    return ans


print(find_longest("aabbcc", 1))
print(find_longest("aabbcc", 2))
print(find_longest("aabbcc", 3))
print(find_longest("aaabbb", 3))
