class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x // 2 + 1
        while l <= r:
            m = l + (r - l) // 2
            sqrVal = m * m
            if sqrVal > x:
                r = m - 1
            else:
                l = m + 1
        return r