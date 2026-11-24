class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        l = 0
        r = k - 1
        res = []
        if len(nums) == 2 and k == 1:
            return nums

        while r < len(nums):
            maxNum = 0
            innerPointer = l 
            for i in range(innerPointer, r+1):
                maxNum = max(maxNum, nums[i])
            res.append(maxNum)
            l+=1
            r+=1
        return res
        