class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        groups = {} # key is a frequency tuple of length 26, value is list of strs matching it

        for s in strs:
            counts = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                counts[index] += 1
            counts_tuple = tuple(counts)
            groups.setdefault(counts_tuple, []).append(s)
        return list(groups.values())