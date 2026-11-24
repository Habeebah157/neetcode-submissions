from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        
        # Step 1: Build graph (list of neighbors for each airport)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Step 2: Sort neighbors lex order
        for src in graph:
            graph[src].sort()
        
        route = []
        
        def visit(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)  
                visit(next_airport)
            route.append(airport)
        
        visit("JFK")
        return route[::-1]
