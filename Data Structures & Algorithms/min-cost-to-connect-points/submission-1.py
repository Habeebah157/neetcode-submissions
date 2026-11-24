class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        visited = set()
        heap = [(0, 0)]  
        total_cost = 0
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost
            for j in range(n):
                if j not in visited:
                    heapq.heappush(heap, (manhattan_distance(points[i], points[j]), j))

        return total_cost

            


        