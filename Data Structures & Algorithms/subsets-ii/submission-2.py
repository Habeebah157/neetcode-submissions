from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort to group duplicates
        res = []
        curr = []

        def helper(i):
            if i == len(nums):
                res.append(curr.copy())  # No need to check duplicates — we avoid them in logic
                return

            # Include nums[i]
            curr.append(nums[i])
            helper(i + 1)
            curr.pop()

            # Skip duplicates: if next elements are same, skip them at this level
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i] (and all duplicates at this level)
            helper(i + 1)

        helper(0)
        return res