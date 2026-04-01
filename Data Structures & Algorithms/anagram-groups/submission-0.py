class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        groups = []
        last_index = -1

        locations = {} # key is index_in_groups, value is counts dict
        for s in strs:
            added = False
            counts = {}
            for char in s:
                counts[char] = counts.get(char, 0) + 1
            for index in locations:
                if locations[index] == counts:
                    groups[index].append(s)
                    added = True
                    break
            if added: 
                continue
            groups.append([s])
            last_index += 1
            locations[last_index] = counts
        print(locations)
        return groups