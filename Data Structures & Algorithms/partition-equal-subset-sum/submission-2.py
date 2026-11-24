class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False 

        capacity = total_sum // 2
        n = len(nums)

        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            weight = nums[i - 1]
            print(i,nums)
            value = weight
            for w in range(capacity + 1):
                if w < weight:
                    dp[i][w] = dp[i - 1][w]  
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

        return dp[n][capacity] == capacity