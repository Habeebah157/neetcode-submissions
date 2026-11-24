class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        array = [[False] * len(s) for _ in range(len(s))]
        max_len = 1
        start = 0

        for i in range(len(s)): 
            array[i][i] = True
        
        for i in range(len(s)-1): 
            if s[i] == s[i+1]: 
                array[i][i+1] = True
                start = i
                max_len = 2

        for k in range(3, n + 1):
            second = n - k + 1
            for i in range(second):
                j = i + k - 1

                if array[i + 1][j - 1] and s[i] == s[j]:
                    array[i][j] = True

                    if k > max_len:
                        start = i
                        max_len = k

        return s[start:start + max_len]


        