# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return 0
            left_h = dfs(node.left, depth + 1)
            right_h = dfs(node.right, depth + 1)
            return 1 + max(left_h, right_h)

        return dfs(root, 0)