class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = l + (r - l) // 2
            dayCount = 1
            curDayWeight = 0
            for w in weights:
                if curDayWeight + w > m:
                    dayCount += 1
                    curDayWeight = 0
                curDayWeight += w
            if dayCount > days:
                l = m + 1
            else:
                r = m - 1
        return l