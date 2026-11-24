from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()  # Helps avoid duplicate combinations
        memo = {}  # Memoization cache: (index, current_sum) -> number of ways

        def helper(index, current_sum):
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            if current_sum == amount:
                return 1
            if current_sum > amount or index >= len(coins):
                return 0
            # Include coins[index] (unlimited) OR skip to next coin
            ways = helper(index, current_sum + coins[index]) + helper(index + 1, current_sum)
            memo[(index, current_sum)] = ways  # Cache the result
            return ways

        return helper(0, 0)