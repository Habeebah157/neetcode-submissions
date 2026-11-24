class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionaryOfIndexandSisterValues={}
        addsUptoINdex = set()
        for i in range(len(nums)):
            dictionaryOfIndexandSisterValues[target-nums[i]] =i 
        index = 0
        for i in range(len(nums)):
            if nums[i] in dictionaryOfIndexandSisterValues and dictionaryOfIndexandSisterValues[nums[i]] != i:
                print(dictionaryOfIndexandSisterValues[nums[i]])
                return [i, dictionaryOfIndexandSisterValues[nums[i]]]
        
        print(dictionaryOfIndexandSisterValues)