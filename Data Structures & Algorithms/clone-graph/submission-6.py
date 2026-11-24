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

        mapping = {}  # original node → cloned node

        # Step 1: DFS to CREATE all clone nodes (no neighbors yet)
        def dfs_create(n):
            if n in mapping:
                return
            mapping[n] = Node(n.val)  # create clone, store it
            for neighbor in n.neighbors:
                dfs_create(neighbor)

        dfs_create(node)

        # Step 2: For each original node, set its clone's neighbors
        for original, clone in mapping.items():
            # clone's neighbors should be the clones of original's neighbors
            clone.neighbors = [mapping[neighbor] for neighbor in original.neighbors]

        # Step 3: Return clone of the input node
        return mapping[node]