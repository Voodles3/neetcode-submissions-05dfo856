class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0] * len(nums)

        product = 1
        zero_index = None
        for i, num in enumerate(nums):
            if num == 0:
                zero_index = i
                continue
            product *= num
        if zero_index:
            out = [0] * len(nums)
            out[zero_index] = product
            return out

        out = [product] * len(nums)

        for i, num in enumerate(nums):
            out[i] = int(out[i] / num)
        return out