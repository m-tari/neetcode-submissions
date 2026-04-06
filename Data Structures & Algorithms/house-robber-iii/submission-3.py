# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(node, par):
            if not node:
                return 0

            if (node, par) in cache:
                return cache[(node, par)]

            excl = dfs(node.right, False) + dfs(node.left, False)
            incl = 0
            if not par:
                incl = node.val + dfs(node.right, True) + dfs(node.left, True)
            res = max(excl, incl)
            cache[(node, par)] = res
            return res

        
        return dfs(root, False)