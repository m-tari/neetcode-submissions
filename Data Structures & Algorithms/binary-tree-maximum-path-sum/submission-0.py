# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = - float("inf")

        def dfs(node):

            if not node:
                return 0

            include = node.val + dfs(node.right) + dfs(node.left)
            exclude = node.val + max(dfs(node.right), dfs(node.left), 0)

            self.res = max(include, self.res)
            return exclude


        dfs(root)

        return self.res