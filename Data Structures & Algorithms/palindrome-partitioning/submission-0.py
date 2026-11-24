class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(whatsleft: str, path: List[str]) -> None:
            nonlocal result  

            if not whatsleft:
                result.append(path[:])

            for i in range(1, len(whatsleft) + 1):
                if self.palindrome(whatsleft[:i]):
                    dfs(whatsleft[i:], path + [whatsleft[:i]])

        dfs(s, [])
        return result

    def palindrome(self, s: str) -> bool:
        return s == s[::-1]