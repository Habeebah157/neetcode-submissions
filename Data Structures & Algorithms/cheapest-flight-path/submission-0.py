class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        array = [float('inf')] * n
        array[src] = 0

        for _ in range(k + 1):  # don't overwrite 'n' variable in loop
            temp = array[:]

            for u, v, w in flights:
                if array[u] == float('inf'):
                    continue
                if array[u] + w < temp[v]:  # corrected here
                    temp[v] = array[u] + w
            array = temp

        return array[dst] if array[dst] != float('inf') else -1