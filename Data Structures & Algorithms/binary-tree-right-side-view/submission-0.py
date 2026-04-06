# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        cur = root
        if cur:
            res.append(cur.val)

        while cur:
            if cur.right:
                cur = cur.right
            elif cur.left:
                cur = cur.left
            else:
                break
            res.append(cur.val)

        return res