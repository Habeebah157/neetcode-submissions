class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doesRepeat= set()
        for i in nums:
            if i in doesRepeat:
                return True
            else:
                doesRepeat.add(i)
        return False
         