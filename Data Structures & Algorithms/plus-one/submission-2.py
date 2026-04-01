class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        while digits[-1] == 10:
            digits.pop()
            result.insert(0, 0)
            
            if not digits:
                result.insert(0, 1)
                return result

            digits[-1] += 1
        result = digits + result
        return result