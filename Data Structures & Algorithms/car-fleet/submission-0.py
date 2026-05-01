class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [7, 4, 1, 0] [1, 2, 2, 5]
        # 

        speeds = {position[i]: num for i, num in enumerate(speed)}
        position.sort(reverse=True)

        stack = []

        for i in range(len(position)):
            cur = position[i]
            time = (target - cur) / speeds[cur]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)