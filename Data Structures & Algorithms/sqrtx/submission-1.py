class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            m = l + (r - l) // 2
            sqrVal = m * m
            print(l)
            print(r)
            print(m, "\n")
            if sqrVal <= x and (m + 1) * (m + 1) > x:
                return m
            elif sqrVal > x:
                r = m - 1
            else:
                l = m + 1
        return m