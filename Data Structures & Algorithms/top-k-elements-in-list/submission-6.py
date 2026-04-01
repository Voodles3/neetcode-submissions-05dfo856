class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        
        out = []
        i = len(buckets) - 1
        while i > 0 and k > 0:
            nums_list = buckets[i]
            if not nums_list:
                i -= 1
                continue
            out.append(nums_list.pop())
            k -= 1
            if nums_list:
                continue
            i -= 1
            if k == 0:
                return out
        return out




