class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i, h in enumerate(heights):
            for j in range(i + 1, len(heights)):
                maxArea = max(maxArea, min(h, heights[j]) * (j - i))
        
        return maxArea