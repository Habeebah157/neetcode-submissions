class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def helper(num):
            if num == len(nums): 
                res.append(curr.copy())
                return 

            curr.append(nums[num])
            helper(num+1)
            curr.pop()
            helper(num+1)

        helper(0)
        return res
        