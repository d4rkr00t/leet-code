# Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# medium


def path_sum(root, sum):
    ans = []

    def dfs(root, path, cur_sum):
        if not root:
            return

        if not root.left and not root.right and cur_sum + root.val == sum:
            ans.append(path + [root.val])
            return

        path.append(root.val)

        dfs(root.left, path, cur_sum + root.val)
        dfs(root.right, path, cur_sum + root.val)

        path.pop()

    dfs(root, [], 0)

    return ans
