import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''

        (0,2)
        (0,0)
        (0-2)/(0-0)
        sqrt((0-0)^2 + (0-2)^2) = sqrt(0+4) = 2

        '''
        origin = [0, 0]
        heap = []
        for point in points:
            distance = math.dist(point, origin)
            heapq.heappush(heap, (distance, point))
        res = []
        for _ in range(k):
            dist, closest_point = heapq.heappop(heap)
            res.append(closest_point)
        return res
        