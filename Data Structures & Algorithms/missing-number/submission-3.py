class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for n in [i for i in range(len(nums) + 1)]:
            if n not in nums:
                return n
        