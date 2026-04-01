class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {k: s.count(k) for k in s}
        chars_t = {k: t.count(k) for k in t}
        return chars_s == chars_t
        