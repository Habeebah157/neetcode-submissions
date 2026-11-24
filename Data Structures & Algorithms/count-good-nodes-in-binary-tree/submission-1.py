# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> bool:
        self.isgood = 0
        self.isGood(root, -1001)
        return self.isgood

    def isGood(self, root, max_value):  # Use `max_value` to avoid overwriting the `max` function
        if not root:
            return
        if root.val >= max_value:
            self.isgood += 1
        max_value = max(root.val, max_value)
        self.isGood(root.left, max_value)
        self.isGood(root.right, max_value)
