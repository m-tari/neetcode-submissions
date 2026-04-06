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

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            include = node.val + left + right
            exclude = node.val + max(left,  right, 0)

            self.res = max(include, self.res)
            return exclude


        dfs(root)

        return self.res