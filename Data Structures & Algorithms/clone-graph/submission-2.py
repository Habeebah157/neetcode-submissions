"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        start = node
        stk = [start]
        visited = set()
        visited.add(start)
        o_to_n = {}

        while stk: 
            old = stk.pop()
            o_to_n[old] = Node(val = old.val)
            for neigh in old.neighbors: 
                if neigh not in visited: 
                    stk.append(neigh)
                    visited.add(neigh)

        for old_node, new_node in o_to_n.items(): 
            for neigh in old_node.neighbors: 
                new_neigh = o_to_n[neigh]
                new_node.neighbors.append(new_neigh)
        
        return o_to_n[start]

