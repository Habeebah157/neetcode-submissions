class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if root is None:
            return True
        
        # Check if current node value is within the valid range
        if not (low < root.val < high):
            return False
        
        # Recursively validate left and right subtrees with updated bounds
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)
