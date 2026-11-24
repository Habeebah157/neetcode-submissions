"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mapping = {}  
        def dfs_create(n: 'Node'):
            if n in mapping:
                return
            mapping[n] = Node(n.val) 
            for neighbor in n.neighbors:
                dfs_create(neighbor)

        dfs_create(node)

        for original, clone in mapping.items():
            clone.neighbors = [mapping[neighbor] for neighbor in original.neighbors]

        return mapping[node]