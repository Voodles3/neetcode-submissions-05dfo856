class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complements:
                if i < complements[complement]:
                    return [i, complements[complement]]
                return [complements[complement], i]
            complements[num] = i
        return []
