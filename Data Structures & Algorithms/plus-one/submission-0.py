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

        # digits will be working copy
        # result will only contain finalized 
        #
        # add 1 to the last digit of [digits]. if it's 10 then remove it, 
        # append a 0 to the start of [result], and repeat. once last digit of [digits] < 10, 
        # append the rest of digits to the start of result and return.

        # ex: 99899. should return 99900.
        # first add 1 to final digit, we get 9 9 8 9 10. it's 10 so remove it.
        # digits is now 9 9 8 9 and result is 0
        # add 1 to last digit again and now digits is 9 9 8 10. it's 10 so remove it.
        # digits is now 9 9 8 and result is 0 0
        # add 1 to last digit and it's now 9 9 9. last digit is not 10, so add
        # to result to get 9 9 9 0 0. success.