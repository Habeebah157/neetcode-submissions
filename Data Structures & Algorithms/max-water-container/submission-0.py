class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        for i, j in enumerate(heights):
            for k, l in enumerate(heights[:-1]):
                width = abs(i-k-1)
                height = min(heights[i], heights[k+1])
                if(width * height > highest):
                    highest = width * height
            
        return highest
        