class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = n
        if n == 0:
            return 1
        elif n < 0:
            m = n * -1
        product = x
        for i in range(m - 1):
            product *= x
        if n < 0:
            return 1 / product
        return product