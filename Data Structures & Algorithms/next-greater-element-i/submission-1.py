class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index = {num: i for i, num in enumerate(nums1)}
        out = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                popped = stack.pop()
                out[nums1_index[popped]] = cur
            if cur in nums1_index:
                stack.append(nums2[i])

        return out