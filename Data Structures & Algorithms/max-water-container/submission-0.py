class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = (right-left)*min(heights[left], heights[right])
        while left < right:
            if heights[left] > heights[right]:
                right -= 1
            else:
                left +=1
            vol = (right-left)*min(heights[left], heights[right])
            if vol > max_vol:
                max_vol = vol
        return max_vol
            