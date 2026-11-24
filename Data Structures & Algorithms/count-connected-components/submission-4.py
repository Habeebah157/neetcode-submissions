from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node): 
            if node in visited: 
                return 

            visited.add(node)
            for i in graph[node]: 
                if i not in visited: 
                    dfs(i)


        graph = defaultdict(list)

        res = 0
        visited = set()

        for i, j in edges: 
            graph[i].append(j)
            graph[j].append(i)
        
        for i in range(n): 
            if i not in visited: 
                dfs(i)
                res+=1

        return res


        


        