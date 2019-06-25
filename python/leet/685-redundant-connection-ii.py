def find_redundant(edges):
    uf = [x for x in range(len(edges))]

    def find_parent(v):
        if uf[v - 1] == v - 1:
            return v - 1

        return find_parent(uf[v - 1] + 1)

    def union(f, t):
        fp = find_parent(f)
        tp = find_parent(t)

        uf[fp] = tp

    def find(f, t):
        return find_parent(f) == find_parent(t)

    redundant = None

    for f, t in edges:
        if find(f, t):
            redundant = [f, t]
        else:
            union(f, t)

    return redundant


# print(find_redundant([[1, 2], [1, 3], [2, 3]]), [2, 3])
# print(find_redundant([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
# print(find_redundant([[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [
#       4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]), [4, 10])
print(find_redundant([[2, 1], [3, 1], [4, 2], [1, 4]]), [2, 1])
