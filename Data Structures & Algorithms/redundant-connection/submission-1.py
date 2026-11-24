from typing import List

class UnionFind:
    def __init__(self, n):
        # Parent array: parent[i] points to the parent of node i
        # Initially, every node is its own parent
        self.parent = list(range(n + 1))

    def find(self, x):
        # Recursive find with path compression
        # If x is not the root, find the root and update x's parent to point directly to it
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # If they are already in the same set, return False (redundant)
        if rootX == rootY:
            return False

        # Simply attach rootY to rootX arbitrarily
        # (Without checking size/rank)
        self.parent[rootY] = rootX
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
        return []