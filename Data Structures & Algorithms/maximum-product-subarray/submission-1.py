class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        rst = nums[0]
        max_val = rst
        min_val = rst
        
        for i in range(1, n):
            cur = nums[i]
            if cur < 0:  # swap max and min
                max_val, min_val = min_val, max_val
            
            min_val = min(cur * min_val, cur)
            max_val = max(cur * max_val, cur)
            rst = max(max_val, rst)
        
        return rst