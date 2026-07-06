class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights)-1
        maxArea = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            maxArea = max(area,maxArea)

            if heights[left] > heights[right]:
                right -= 1
            
            elif heights[right] > heights[left]:
                left += 1 
            
            else:
                right -= 1
                left += 1
        
        return maxArea
