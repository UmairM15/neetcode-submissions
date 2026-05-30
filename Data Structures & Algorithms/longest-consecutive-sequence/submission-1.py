from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0

        for n in nums:
            if n - 1 not in numsSet:
                i = n
                seqLen = 1
                while i + 1 in numsSet:
                    seqLen += 1
                    i += 1
                
                if seqLen > maxLen:
                    maxLen = seqLen
        
        return maxLen
