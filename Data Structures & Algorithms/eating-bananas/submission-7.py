class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 0
        for b in piles:
            r = max(r, b)
        while l <= r:
            curTime = 0
            k = l + (r - l) // 2
            for b in piles:
                curTime += (b + k - 1) // k
            if curTime <= h:
                r = k - 1
            else:
                l = k + 1
        return l