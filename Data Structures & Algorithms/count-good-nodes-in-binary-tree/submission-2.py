# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]  # We'll use this like a global counter
        
        def dfs(smallest, node):
            if not node:
                return
            
            # ✅ FIXED: Check if current node is GOOD (>= max so far)
            if node.val >= smallest:
                count[0] += 1  # ✅ FIXED: += 1, not +1 (this actually changes the value!)
            
            # ✅ FIXED: Always recurse on BOTH children, with updated max
            new_smallest = max(smallest, node.val)
            dfs(new_smallest, node.left)
            dfs(new_smallest, node.right)
        
        # Start DFS from root with initial smallest = root.val
        dfs(root.val, root)
        
        return count[0]
        