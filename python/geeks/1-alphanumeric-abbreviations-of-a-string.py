# Alphanumeric Abbreviations of a String
# url: https://www.geeksforgeeks.org/alphanumeric-abbreviations-of-a-string/


def abbr_str(s):
    if len(s) == 0:
        return []

    ans = set([s])

    if len(s) == 1:
        ans.add(str(1))
        return list(ans)

    def rec_abbr(s, pos, prev, count):
        if pos >= len(s):
            return ans.add(prev)

        if prev and prev[-1].isdigit():
            rec_abbr(s, pos + 1, prev + s[pos], count)
            new_str = list(prev)
            prev_count = int(new_str[-1])
            new_str[-1] = str(prev_count + 1)
            rec_abbr(s, pos + 1, "".join(new_str), count + 1)
        else:
            rec_abbr(s, pos + 1, prev + s[pos], count)
            rec_abbr(s, pos + 1, prev + str(count), count)

    rec_abbr(s, 0, "", 1)

    return list(ans)


print(abbr_str("ANKS"))
