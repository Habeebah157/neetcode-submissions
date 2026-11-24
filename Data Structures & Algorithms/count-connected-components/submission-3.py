class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # array = []
        # count = 0
        # edges.sort(key = lambda x: x[0])
        # if n == 1: 
        #     return 1
        # for i in edges: 
        #     print("i",i)
        #     print(array)
        #     if len(array) == 0: 
        #         array.append(i)
        #         print("Here", array)
        #     else: 
        #             if i[0] in array[-1] or i[1] in array[-1]:
        #                 array.append(i)
        #             else: 
        #                 print("YELLO")
        #                 count+=1
        #                 del array[:]
        #                 array.append(i)
        #                 print(array)
        # print(array)
        # if len(array) > 0: 
        #     print("YEL")
        #     count+=1
        # return count

        component = 0
        visited = set()
        graph = {node: [] for node in range(n)}
        for edge1, edge2 in edges: 
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        print(graph)

        def dfs(node): 
            for neighbour in graph[node]: 
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for i in graph: 
            if i in visited: 
                continue
            else: 
                visited.add(i)
                component+=1
                dfs(i)

        return component
                

        

        

        