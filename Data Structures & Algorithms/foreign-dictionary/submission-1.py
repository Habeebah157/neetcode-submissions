from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Get all unique characters
        chars = set(''.join(words))
        if not chars:
            return ""
        
        # Step 2: Build graph using SETS to avoid duplicate edges
        graph = {c: set() for c in chars}  # 👈 use set() instead of list
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            # Invalid: prefix comes after longer word
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            # Find first differing char
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].add(c2)  # 👈 add (no duplicates)
                    break

        visiting = set()
        output = []

        def dfs(c):
            if c in visiting:
                return False
            if not graph[c]:  # empty set
                if c not in output:  # safety (optional, but robust)
                    output.append(c)
                return True

            visiting.add(c)
            for nb in graph[c]:
                if not dfs(nb):
                    return False
            visiting.remove(c)

            graph[c].clear()  # mark as safe
            if c not in output:  # prevent duplicates
                output.append(c)
            return True

        for c in chars:
            if not dfs(c):
                return ""

        return ''.join(reversed(output))
