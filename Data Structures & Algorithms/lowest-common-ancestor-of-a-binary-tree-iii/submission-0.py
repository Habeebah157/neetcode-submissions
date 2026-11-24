"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        stkp = []
        stkq = []
        prev = None

        while p != None or q != None: 
            if p: 
                stkp.append(p)
                p = p.parent
            if q: 
                stkq.append(q)
                q = q.parent

        while stkp and stkq: 
            if stkp[-1].val == stkq[-1].val: 
                prev = stkp.pop()
                stkq.pop()
            else: 
                break
        return prev
        