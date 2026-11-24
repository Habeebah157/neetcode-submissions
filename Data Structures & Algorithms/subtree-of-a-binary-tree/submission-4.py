# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p, q):
            # Base cases
            if not p and not q:
                return True
            if not p or not q:
                return False
            # Check values and recursively check subtrees
            return (p.val == q.val and 
                    isSame(p.left, q.left) and 
                    isSame(p.right, q.right))

        def dfs(node):
            # If node is None, then no subtree possible here
            if not node:
                return False
            
            # Check if current node matches subRoot exactly
            if isSame(node, subRoot):
                return True
            
            # Recursively check left and right subtrees
            return dfs(node.left) or dfs(node.right)

        # Start DFS from root
        return dfs(root)
