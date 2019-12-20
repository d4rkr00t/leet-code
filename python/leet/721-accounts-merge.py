# Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# medium
#
# Time:  O(n^2) – n number of accounts
# Space: O(n)
#
# Solution:
# Graph + Connected components

def accountsMerge(accounts: [[str]]) -> [[str]]:
    if not accounts:
        return []

    # 1. Build a graph email -> email
    graph = {}

    for group in accounts:
        name = group.pop(0)
        for email in group:
            graph[email] = { 'name': name, 'connections': set() } if not email in graph else graph[email]
            for connection in group:
                if connection != email:
                    graph[email]['connections'].add(connection)

    # 2. Connected components
    def getConnected(graph, visited, start, result):
        visited.add(start)
        result.append(start)

        for email in graph[start]['connections']:
            if email in visited:
                continue

            getConnected(graph, visited, email, result)

        return result

    visited = set()
    result = []

    for email in graph.keys():
        if email in visited:
            continue

        name = graph[email]['name']
        emails = getConnected(graph, visited, email, [])
        res = [name]
        res.extend(list(sorted(emails)))
        result.append(res)

    return result


print(
    accountsMerge(
        [
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
    )
)
