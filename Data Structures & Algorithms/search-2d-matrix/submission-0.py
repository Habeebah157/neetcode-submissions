class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m= 0, len(nums)-1, 0

        if len(nums) == 1:
            if target == nums[0]:
                return True
        if len(nums) == 2:
            if target in nums:
                if target == nums[0]:
                    return True
                else:
                    return True
        
        while l < r and r-l > 1:
            m = (l+r)//2
            if target == nums[l]:
                return True
            if target == nums[r]:
                return True
            if target == nums[m]:
                return True
            if nums[m] < target:
                l = m
            if nums[m] > target:
                r = m
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #What should I return if not a 2d. 
        #What should I return if just 1D, 
        # Can I change it to a 1d array? 
        # So it wouldn't always be a square right? 
        newMatrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newMatrix.append(matrix[i][j])
        if target not in newMatrix:
            return False
        else: 
            res = self.search(newMatrix, target)
            return res
        