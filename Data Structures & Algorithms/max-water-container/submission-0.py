class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculateArea(l, r):
            low = min(heights[l], heights[r])
            return low * (r - l)
        
        l, r = 0, len(heights) - 1
        max_area = 0
        
        while l < r:
            current_area = calculateArea(l, r)
            max_area = max(max_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
