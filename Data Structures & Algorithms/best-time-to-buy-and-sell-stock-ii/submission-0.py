class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        prof = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i + 1]:
                j = i + 1
                while j < len(prices) - 1 and prices[j] < prices[j + 1]:
                    j += 1
                
                prof += prices[j] - prices[i]
                i = j
            i += 1

        return prof