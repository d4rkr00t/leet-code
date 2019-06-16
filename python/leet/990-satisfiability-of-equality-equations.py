# Satisfiability of Equality Equations
# url: https://leetcode.com/problems/satisfiability-of-equality-equations/
# medium


def equations_possible(equations):
    graph = {}
    colors = {}

    for e in equations:
        l = e[0]
        r = e[3]
        is_eq = e[1] != '!'

        if not l in graph:
            graph[l] = []

        if not r in graph:
            graph[r] = []

        if is_eq:
            graph[l].append(r)
            graph[r].append(l)

    next_color = 0
    for v in graph.keys():
        if v in colors:
            continue

        stack = [v]
        next_color += 1

        while stack:
            cur = stack.pop(0)
            colors[cur] = next_color
            for sv in graph[cur]:
                if not sv in colors:
                    stack.append(sv)

    for e in equations:
        l = e[0]
        r = e[3]
        is_eq = e[1] != '!'

        if not is_eq and colors[l] == colors[r]:
            return False

    return True


print(equations_possible(["a==b", "b!=a"]), False)
print(equations_possible(
    ["a==b", "b==a", "c==e", "e==a", "f==e", "f!=a", "c!=b"]), False)
print(equations_possible(["a==b", "b==c", "c==a"]), True)
print(equations_possible(["c==c", "b==d", "x!=z"]), True)
print(equations_possible(["a==b", "b!=c", "c==a"]), False)
print(equations_possible(["a!=a"]), False)
print(equations_possible(["a!=b", "b!=c", "c!=a"]), True)
print(equations_possible(["b==b", "b==e", "e==c", "d!=e"]), True)
print(equations_possible(
    ["f==d", "b!=e", "d!=c", "b==c", "b!=a", "b!=f"]), True)
