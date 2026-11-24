class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m= 0, len(nums)-1, 0

        if len(nums) == 1:
            if target == nums[0]:
                return 0
        if len(nums) == 2:
            if target in nums:
                if target == nums[0]:
                    return 0
                else:
                    return 1
        
        while l < r and r-l > 1:
            m = (l+r)//2
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target == nums[m]:
                return m
            if nums[m] < target:
                l = m
            if nums[m] > target:
                r = m
        return -1
        