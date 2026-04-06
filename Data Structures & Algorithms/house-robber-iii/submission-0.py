# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node, par):
            if not node:
                return 0

            excl = dfs(node.right, False) + dfs(node.left, False)
            incl = 0
            if not par:
                incl = max(
                    node.val + dfs(node.right, True), 
                    node.val + dfs(node.left, True)
                )

            return max(excl, incl)

        
        return dfs(root, False)