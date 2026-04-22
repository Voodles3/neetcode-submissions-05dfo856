class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights) - 1
        while right > left:
            diff = right - left
            water = diff * min(heights[left], heights[right])
            if water > max_water:
                max_water = water
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_water