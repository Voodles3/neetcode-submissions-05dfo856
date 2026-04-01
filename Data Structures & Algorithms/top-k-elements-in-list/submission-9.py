class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int) # key = num, value = frequency

        for n in nums:
            frequencies[n] += 1
        
        freq_tuples = [(f, n) for n, f in frequencies.items()]
        freq_tuples.sort(reverse=True)
        print(freq_tuples)
        out = []
        for i in range(k):
            out.append(freq_tuples[i][1])
        return out
            