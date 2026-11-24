class Solution:
    def findMin(self, nums: List[int]) -> int:
        #What happens with an empty array or an array of just one. 
        #What happens with 
        #Could the smallest number be a negative. 
        nums.sort()
        return nums[0]
        