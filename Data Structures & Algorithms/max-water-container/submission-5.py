class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(heights)-1

        while left < right:
            width = right - left
            area = width * min(heights[right],heights[left])
            maxA = area if area > maxA else maxA

            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxA
