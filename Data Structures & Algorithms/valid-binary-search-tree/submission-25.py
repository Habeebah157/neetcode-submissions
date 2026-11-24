# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = [True]

        def dfs(root, min_allowed, max_allowed):
            if not root: 
                return 

            if root.val <= min_allowed or root.val >= max_allowed:
                res[0] = False
                return

            if root.right and root.right.val < root.val:
                res[0] = False
                return

            if root.left and root.left.val > root.val:
                res[0] = False
                return

            dfs(root.left, min_allowed, root.val)
            dfs(root.right, root.val, max_allowed)

        dfs(root, float('-inf'), float('inf'))
        return res[0]