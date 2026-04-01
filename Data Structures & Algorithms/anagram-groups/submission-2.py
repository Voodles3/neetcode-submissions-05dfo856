class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        print(out)
        anagrams = {} # key = sorted anagram, value = index in out list

        for s in strs:
            srted = str(sorted(s))
            if srted not in anagrams:
                index = len(out)
                out.append([s])
                anagrams[srted] = index
            else:
                index = anagrams[srted]
                out[index].append(s)
        return out