class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            complement = target - num
            try: 
                comp_index = numbers.index(complement)
                if i == comp_index:
                    continue
                return [i+1, comp_index+1] if i < comp_index else [comp_index + 1, i+1]
            except ValueError:
                continue
            