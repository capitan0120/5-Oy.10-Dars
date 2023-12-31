class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            q = n%4
            if q:
                return False
            n //= 4
        return True