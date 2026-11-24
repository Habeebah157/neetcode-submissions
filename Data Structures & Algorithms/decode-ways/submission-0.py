class Solution:
    def numDecodings(self, s: str) -> int:
        # So this one is like first we take the first word if it is not 0: 
        # Then we check check for the first element, if it can be 
        if s[0] == "0": 
            return 0
        dp = [1, 1]
        for ind, num in enumerate(s[1:], 2): 
            print(ind, num)
            ways = 0
            if num != "0": 
                ways += dp[ind-1]
            if 10 <= int(s[ind-2] + num) <= 26: 
                ways += dp[ind-2]
            dp.append(ways)
        return dp[-1]