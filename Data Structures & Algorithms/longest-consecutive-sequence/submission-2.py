from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                seqLen = 1
                while n + seqLen in numsSet:
                    seqLen += 1
                
                maxLen = max(maxLen, seqLen)
        
        return maxLen
