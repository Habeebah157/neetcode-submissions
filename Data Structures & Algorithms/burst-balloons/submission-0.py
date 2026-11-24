class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # Add boundary balloons
        n = len(nums)
        
        # Create a memoization table initialized with -1
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        
        def dfs(left: int, right: int) -> int:
            # Base case: no balloons between left and right
            if left + 1 >= right:
                return 0
            
            # Return memoized result if available
            if memo[left][right] != -1:
                return memo[left][right]
            
            max_coins = 0
            # Try every balloon in (left, right) as the last to burst
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right]  # Current burst
                coins += dfs(left, i) + dfs(i, right)      # Left and right subproblems
                max_coins = max(max_coins, coins)
            
            # Store result in memo table before returning
            memo[left][right] = max_coins
            return max_coins
        
        return dfs(0, n - 1)  # Solve for the entire range