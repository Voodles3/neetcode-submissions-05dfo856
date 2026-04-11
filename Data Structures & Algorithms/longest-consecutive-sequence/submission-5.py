class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_length = 0
        curr_length = 1
        prev_num = nums[0]
        for num in nums[1:]:
            if prev_num + 1 == num:
                curr_length += 1
            elif prev_num == num:
                continue
            else:
                longest_length = max(curr_length, longest_length)
                curr_length = 1
            prev_num = num
        longest_length = max(curr_length, longest_length)
        return longest_length