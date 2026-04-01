class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += f"{len(s)}!{s}"
        return out

    def decode(self, s: str) -> List[str]:
        index = 0
        out = []
        while index < len(s):
            num = ""
            while s[index] != "!":
                num += s[index]
                index += 1
            index += 1
            length = int(num)
            out.append(s[index:index+length])
            index += length
        return out
        