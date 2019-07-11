# Clone Graph
# https://leetcode.com/problems/clone-graph/
# medium


def cloneGraph(node):
    def clone(node):
        if '$ref' in node:
            return {'$ref': node['$ref']}

        new_node = {
            '$id': node['$id'],
            'neighbors': [clone(n) for n in node['neighbors']]
        }

        return new_node

    return clone(node)


print(cloneGraph({"$id": "1", "neighbors": [{"$id": "2", "neighbors": [{"$ref": "1"}, {"$id": "3", "neighbors": [{"$ref": "2"}, {
      "$id": "4", "neighbors": [{"$ref": "3"}, {"$ref": "1"}], "val": 4}], "val": 3}], "val": 2}, {"$ref": "4"}], "val": 1}))
