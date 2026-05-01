class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = {i: len(heights) - i - 1 for i in range(len(heights))}
        left = {i: i for i in range(len(heights))}

        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                val = stack.pop()
                right[val] = i - val - 1
            stack.append(i)
        
        stack.clear()
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                val = stack.pop()
                left[val] = val - i - 1
            stack.append(i)

        max_area = 0
        for i, h in enumerate(heights):
            area = h * (right[i] + left[i] + 1)
            max_area = max(max_area, area)
        return max_area