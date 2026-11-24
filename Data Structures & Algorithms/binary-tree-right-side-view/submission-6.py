# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        queue = deque([root])
        res = []
        final = []

        while queue: 
            length = len(queue)
            currLev = []
            
            for _ in range(length): 
                temp = queue.popleft()
                currLev.append(temp.val)
                if temp.left: 
                    queue.append(temp.left)
                if temp.right: 
                    queue.append(temp.right)
            
            final.append(currLev[-1])
            res.append(currLev)

        return final