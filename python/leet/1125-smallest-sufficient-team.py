# Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def smallestSufficientTeam(req_skills: [str], people: [[str]]) -> [int]:
    n, m = len(req_skills), len(people)
    key = {v: i for i, v in enumerate(req_skills)}
    dp = {0: []}
    for i, p in enumerate(people):
        his_skill = 0
        for skill in p:
            if skill in key:
                his_skill |= 1 << key[skill]
        if his_skill == 0:
            continue
        if his_skill in dp and len(dp[his_skill]) == 1:
            continue
        for skill_set, need in list(dp.items()):
            with_him = skill_set | his_skill
            if with_him == skill_set: continue
            if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                dp[with_him] = need + [i]
    return dp[(1 << n) - 1]


print(smallestSufficientTeam(
    req_skills = ["java"],
    people = [["java"]]), [0])

print(smallestSufficientTeam(
    req_skills = ["java","nodejs","reactjs"],
    people = [["java"],["nodejs"],["nodejs","reactjs"]]), [0,2])

print(smallestSufficientTeam(
    req_skills = ["mmcmnwacnhhdd","vza","mrxyc"],
    people = [["mmcmnwacnhhdd"],[],[],["vza","mrxyc"]]), [0,3])

print(smallestSufficientTeam(
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
    people = [
        ["algorithms","math","java"],
        ["algorithms","math","reactjs"],
        ["java","csharp","aws"],
        ["reactjs","csharp"],
        ["csharp","math"],
        ["aws","java"]]), [1,2])

#
#
#   java        nodejs        reactjs
#
#
#  [java]      [nodejs]     [nodejs, reactjs]
#
#   java nodejs reactjs
# 0 1    0      0
# 1 0    1      0
# 2 0    1      1
#
# 100: [0]
# 010: [1]
# 011: [2]
#
#
# 1 1 1 0 0 0
# 1 1 0 1 0 0
# 0 0 1 0 1 1
# 0 0 0 1 1 0
# 0 1 0 0 1 0
# 0 0 1 0 0 1
