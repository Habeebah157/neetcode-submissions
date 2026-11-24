class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        print(nums)
        isDuplicate = set()
        for i in nums:
            if i in isDuplicate:
                return i
            else:
                isDuplicate.add(i)