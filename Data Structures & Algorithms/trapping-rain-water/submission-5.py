class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left_wall = 0
        total_area = 0
        water_for_height = defaultdict(int) # key: height, value: water to be added for that height
        prev_height = 0

        for h in height:
            if h < highest_left_wall:
                for i in range(h + 1, highest_left_wall + 1):
                    water_for_height[i] += 1
            if h > prev_height:
                for i in range(1, h + 1):
                    total_area += water_for_height[i]
                    water_for_height[i] = 0
            highest_left_wall = max(highest_left_wall, h)
            prev_height = h
        return total_area