"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_map = {}

        # Phase 1: Clone all nodes (without setting neighbors yet)
        def dfs(n):
            if n in clone_map:
                return
            clone_map[n] = Node(n.val)
            for neighbor in n.neighbors:
                dfs(neighbor)

        dfs(node)

        # Phase 2: Wire up the neighbors using the clone_map
        for original_node, cloned_node in clone_map.items():
            cloned_node.neighbors = [clone_map[neighbor] for neighbor in original_node.neighbors]

        return clone_map[node]