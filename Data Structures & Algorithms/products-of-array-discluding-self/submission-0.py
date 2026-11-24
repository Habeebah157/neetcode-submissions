class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        valueMultiply = []
        excludeNum = 0
        while excludeNum != len(nums):
            multipy = 1
            for i in range(len(nums)):
                if i != excludeNum:
                    multipy *= nums[i]
            valueMultiply.append(multipy)
            excludeNum+=1

        return valueMultiply
        