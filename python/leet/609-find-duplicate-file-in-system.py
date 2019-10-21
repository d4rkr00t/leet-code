# Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/
# medium
#
# Time:  O(n + m) – where n -> number of files, m -> number of duplicate groups
# Space: O(n) - where n -> number of files
#
# Solution:
# – HashTable

from collections import defaultdict


def findDuplicate(self, paths: [str]) -> [[str]]:
    dict = defaultdict(list)  # {}

    def get_file_info(dir_path, file):
        if not file:
            return ("", False)

        file_info = file.split('(')
        return (dir_path + '/' + file_info[0], file_info[1][0:-1] if len(file_info) > 1 else "")

    for path in paths:  # "root/a 1.txt(abcd) 2.txt(efgh)"
        dir_info = path.split(' ')
        dir_path, files = dir_info[0], dir_info[1:]

        for file in files:
            (path, content) = get_file_info(dir_path, file)
            if content:
                dict[content].append(path)

    result = []

    for (key, value) in dict.items():
        if len(value) > 1:
            result.append(value)

    return result


# I: ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# O: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
