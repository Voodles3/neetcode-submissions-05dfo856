import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            heapq.heappush(max_heap, (count*-1, num))
        
        out = []
        for _ in range(k):
            out.append(heapq.heappop(max_heap)[1])
        return out