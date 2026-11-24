class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # odd total sum can’t be partitioned equally

        capacity = total_sum // 2
        n = len(nums)

        # Initialize dp table
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            weight = nums[i - 1]
            value = weight
            for w in range(capacity + 1):
                if w < weight:
                    dp[i][w] = dp[i - 1][w]  # can’t take current item
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

        # Check if exact partition possible
        return dp[n][capacity] == capacity