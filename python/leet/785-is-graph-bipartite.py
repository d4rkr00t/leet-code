# Is Graph Bipartite?
# url: https://leetcode.com/problems/is-graph-bipartite/
# medium

# b    r
# 0----1
# |    |
# |    |
# 3----2
# r    b

# b    r
# 0----1
# | \  |
# |  \ |
# 3----2
# r    r


def is_bipartite(graph):
    colors = [None] * len(graph)

    def color_graph(graph, root):
        nonlocal colors

        stack = [root]
        colors[root] = True

        while stack:
            v = stack.pop(0)
            edges = graph[v]
            color = colors[v]
            next_color = not color

            for e in edges:
                if (colors[e] == color):
                    return False
                elif (colors[e] == None):
                    colors[e] = next_color
                    stack.append(e)

        return True

    for (x, i) in enumerate(graph):
        if colors[x] == None:
            if not color_graph(graph, x):
                return False

    return True


print(is_bipartite([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [
      6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]))
