# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answers = [True]
        def height(root): 
            if root == None: 
                return 0
            left = height(root.left)
            print(left)
            right = height(root.right)
            print(right)
            if abs(left - right) <= 1: 
                answers.append(True)
            else: 
                answers.append(False)

            return 1+max(right, left)
        height(root)
        if False in answers: 
            return False
        else:
            return True
        print(answers)

