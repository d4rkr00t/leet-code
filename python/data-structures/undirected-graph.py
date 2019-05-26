class UDGraph:
    def __init__(self):
        self.vertexes = []
        self.v_to_idx = {}

    def add_edge(self, v, w):
        if not v in self.v_to_idx:
            self.v_to_idx[v] = len(self.vertexes)
            self.vertexes.append(set())

        if not w in self.v_to_idx:
            self.v_to_idx[w] = len(self.vertexes)
            self.vertexes.append(set())

        v_idx = self.v_to_idx[v]
        w_idx = self.v_to_idx[w]

        self.vertexes[v_idx].add(w)
        self.vertexes[w_idx].add(v)

    def get_adj(self, v):
        v_idx = self.v_to_idx[v]
        return list(self.vertexes[v_idx])

    def bfs(self, v, visitor):
        return self.__bfs(v_from=v, visitor=visitor)

    def __bfs(self, v_from, v_to=False, visitor=False, return_parent=False):
        v_idx = self.v_to_idx[v_from]
        discovered = [False] * len(self.vertexes)
        parent = [-1] * len(self.vertexes)
        stack = [v_from]

        discovered[v_idx] = True
        parent[v_idx] = v_idx

        while len(stack):
            vtx = stack.pop(0)
            vtx_idx = self.v_to_idx[vtx]
            adj = self.vertexes[vtx_idx]
            if (visitor):
                visitor(vtx, parent[vtx_idx])

            for v in adj:
                v_idx = self.v_to_idx[v]
                if (not discovered[v_idx]):
                    discovered[v_idx] = True
                    parent[v_idx] = vtx
                    stack.append(v)

                    if v_to and v_to == v:
                        stack = []
                        break

        if (return_parent):
            return parent

    def path(self, v, w):
        parent = self.__bfs(v_from=v, v_to=w, return_parent=True)
        res = [w]
        cur = w

        while (cur != v):
            cur_idx = self.v_to_idx[cur]
            cur = parent[cur_idx]
            res.append(cur)

        return list(reversed(res))

    def __str__(self):
        return str(self.vertexes)


graph = UDGraph()

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 4)
graph.add_edge(1, 3)
graph.add_edge(4, 3)
graph.add_edge(1, 2)
graph.add_edge(3, 2)

print('Graph')
print(graph)
print()

print('Adj to 0', graph.get_adj(0))

print()
print('BFS:')
graph.bfs(0, lambda v, p: print('Visited', v, 'from', p))

print()
print('Path:')
print(graph.path(0, 3))
