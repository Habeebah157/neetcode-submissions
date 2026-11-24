class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opposite = defaultdict(int)
        for i in range(len(nums)): 
            opposite[nums[i]] = i
        print(opposite)
        
        for i in range(len(nums)): 
            sister = target - nums[i]
            if sister in opposite and opposite[sister] != i: 
                return sorted([opposite[sister], i])
