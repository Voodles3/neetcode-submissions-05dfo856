class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                res = sum((nums[i], nums[j], nums[k]))
                if res == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in out:
                        out.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif res > 0:
                    k -= 1
                else:
                    j += 1
        return out

