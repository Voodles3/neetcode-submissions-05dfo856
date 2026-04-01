class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for n in range(len(nums) + 1):
            if n not in nums:
                return n
        