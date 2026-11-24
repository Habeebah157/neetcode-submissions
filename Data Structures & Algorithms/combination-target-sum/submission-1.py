class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(index):
            if sum(curr) == target:
                res.append(curr.copy())  # ✅ COPY!
                return

            if index == len(nums) or sum(curr) > target:  # ✅ == not =
                return

            curr.append(nums[index])
            dfs(index)     # ✅ reuse same index (can reuse numbers!)
            curr.pop()
            dfs(index + 1)

        dfs(0)
        return res