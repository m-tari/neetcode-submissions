# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(node):
            if not node:
                return 0

            if node in cache:
                return cache[node]

            # skip this
            excl = dfs(node.right) + dfs(node.left)

            # rob this
            incl = node.val
            if node.left:
                incl += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                incl += dfs(node.right.left) + dfs(node.right.right)

            res = max(excl, incl)
            cache[node] = res
            return res

        
        return dfs(root)