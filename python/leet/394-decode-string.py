# Decode String
# https://leetcode.com/problems/decode-string/
# medium


def decode_str(s):  # 3[a2[c]]
    if not s:
        return ""

    stack = []  # []

    for c in s:  # 3
        if c != ']':
            stack.append(c)
            continue

        tmp_str = ""  # acc
        while stack and stack[-1] != '[':
            tmp_str = stack.pop() + tmp_str

        stack.pop()  # [

        num = ""  # 3
        while stack and stack[-1].isdigit():  # 3
            num = stack.pop() + num

        num = int(num)

        result_str = ""
        for i in range(num):
            result_str += tmp_str

        stack.append(result_str)  # acc

    tmp_str = ""
    while stack:
        tmp_str = stack.pop() + tmp_str

    return tmp_str


print(decode_str("3[a2[c]]"), "accaccacc")
print(decode_str("3[a]2[bc]"), "aaabcbc")
print(decode_str("2[abc]3[cd]ef"), "abcabccdcdcdef")
# print(decode_str("100[leetcode]"))
