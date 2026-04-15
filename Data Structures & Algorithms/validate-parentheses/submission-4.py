class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for char in s:
            if char in opens:
                stack.append(char)
                continue
            if not stack or char != opens[stack.pop()]:
                return False
        return not stack