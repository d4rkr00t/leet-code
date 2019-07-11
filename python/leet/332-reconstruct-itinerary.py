# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
# medium
import collections


def findItinerary(tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]


print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], [
      "LHR", "SFO"]]), ["JFK", "MUC", "LHR", "SFO", "SJC"])

print(findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], [
      "ATL", "JFK"], ["ATL", "SFO"]]), ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
