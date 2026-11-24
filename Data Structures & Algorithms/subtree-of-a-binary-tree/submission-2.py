# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
    
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot: 
#             return True
#         if not root: 
#             return False

#         if self.sameTree(root, subRoot): 
#             return True
        
#         return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
#     def sameTree(self,root:Optional[TreeNode], subroot:Optional[TreeNode]) -> bool: 
#         if not root and not subRoot: 
#             return True
#         if root is None: 
#             print("Here root",subroot, root)
#             return False
#         if subroot is None: 
#             print("Here subroot",root,)
#             return False

#         return self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right) 
        

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # An empty tree is a subtree of any tree
            return True
        if not root:  # If the root is None, it can't contain any subtree
            return False

        if self.sameTree(root, subRoot): 
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot: 
            return True
        if root is None: 
            print("Here root", subRoot, root)
            return False
        if subRoot is None: 
            print("Here subRoot", root, subRoot)
            return False
        if root.val != subRoot.val: 
            return False

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
