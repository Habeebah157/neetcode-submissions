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

        clone_map = {}

        # Phase 1: Clone all nodes recursively
        def dfs(n):
            if n in clone_map:
                return
            clone_map[n] = Node(n.val)
            for neighbor in n.neighbors:
                dfs(neighbor)

        dfs(node)

        # Phase 2: Wire up neighbors using a simple for loop (no list comprehension)
        for original_node, cloned_node in clone_map.items():
            cloned_node.neighbors = []  # reset (though it's already empty)
            for neighbor in original_node.neighbors:
                cloned_node.neighbors.append(clone_map[neighbor])

        return clone_map[node]