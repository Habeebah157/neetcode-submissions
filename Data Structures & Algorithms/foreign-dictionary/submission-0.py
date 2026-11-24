class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        hrn
        hrf
        er
        
        h - r - n

        h: r, f
        r: n
        f: 
        '''
        adj = defaultdict(set) 
        indegree = {}          
        for w in words:
            for c in w:
                indegree.setdefault(c, 0)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            found_diff = False
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b] += 1
                    found_diff = True
                    break

            if not found_diff and len(w1) > len(w2):
                return ""

        q = deque([c for c in indegree if indegree[c] == 0])
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(result) != len(indegree):
            return ""  
        return "".join(result)
            