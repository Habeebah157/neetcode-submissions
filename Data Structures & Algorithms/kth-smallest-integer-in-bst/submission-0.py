# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = [0]  # Counter to track the position of the current node in the traversal
        result = [None]  # Placeholder for the kth smallest element

        def element(root): 
            if not root: 
                return 
            # Traverse the left subtree
            element(root.left)
            # Increment the counter
            count[0] += 1
            # Check if this is the kth smallest element
            if count[0] == k: 
                result[0] = root.val
                return
            # Traverse the right subtree
            element(root.right)

        element(root)
        return result[0]


            