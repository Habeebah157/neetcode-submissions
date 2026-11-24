class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        copy = []
        def dfs(i):
            print(i >= len(nums))
            print(i)
            if i >= len(nums):
                print(subset)
                copy.append(subset[:]) 
                print("copy", copy)
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        print(copy)
        return copy

        