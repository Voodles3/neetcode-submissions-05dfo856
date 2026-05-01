class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = [nums2[0]]

        for i in range(1, len(nums2)):
            if not stack:
                stack.append(nums2[i])
                continue
            
            while stack and stack[-1] < nums2[i]:
                next_greater[stack.pop()] = nums2[i]

            stack.append(nums2[i])
            
        out = []
        for num in nums1:
            out.append(next_greater.get(num, -1))
        return out