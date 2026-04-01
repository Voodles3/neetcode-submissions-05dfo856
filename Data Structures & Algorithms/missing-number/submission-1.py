class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        required = [i for i in range(len(nums) + 1)]
        for n in required:
            if n not in nums:
                return n
        