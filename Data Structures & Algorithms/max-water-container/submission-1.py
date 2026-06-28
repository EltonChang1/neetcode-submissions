class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0

        while right > left:
            width = right - left
            length = min(heights[right],heights[left])
            area = width*length
            if area > maxArea:
                maxArea = area
            if heights[right] < heights[left]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            elif heights[right] == heights[left]:
                right -= 1
                left += 1
        
        return maxArea

        