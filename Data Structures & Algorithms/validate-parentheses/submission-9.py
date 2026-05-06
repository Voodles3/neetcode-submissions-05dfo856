class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in open_to_closed:
                stack.append(char)
            else:
                if not stack or char != open_to_closed[stack.pop()]:
                    return False
        return not stack