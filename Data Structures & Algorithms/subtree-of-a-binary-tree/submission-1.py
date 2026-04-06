# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def sameTree(node, target_node): 
            # If both are None, they are equal           
            if not node and not target_node:
                return True

            # If one of them is None, they are not equal 
            if not node or not target_node:
                return False

            if node.val == target_node.val:
                left = sameTree(node.left, target_node.left)
                right = sameTree(node.right, target_node.right)
            else:
                return False

            return left and right

        def dfs(node):
            if not node:
                return False

            same = sameTree(node, subRoot)

            if same:
                return True

            lsame = dfs(node.left)
            rsame = dfs(node.right)

            return lsame or rsame

        return dfs(root)

        