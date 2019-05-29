# Longest Possible Chunked Palindrome
# url: https://www.geeksforgeeks.org/longest-possible-chunked-palindrome/


def longest_palindrome(input):
    start = 0
    end = cur = len(input) - 1
    ans = 0

    while (start <= cur):
        if (start == cur):
            ans += 1
            break

        if (input[start] == input[cur]):
            left = input[start:start+end+1-(cur)]
            right = input[cur:end+1]

            if (left == right):
                ans += 2
                start = start+end+1-(cur)
                cur -= 1
                end = cur
            else:
                ans += 1
                break
        else:
            cur -= 1

    return ans


print(longest_palindrome("V"), 1)
print(longest_palindrome("ghiabcdefhelloadamhelloabcdefghi"), 7)
print(longest_palindrome("merchant"), 1)
print(longest_palindrome("antaprezatepzapreanta"), 11)
print(longest_palindrome("geeksforgeeks"), 3)
