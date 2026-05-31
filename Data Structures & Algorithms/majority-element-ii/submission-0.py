from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)
        res = []
        cutoff = int(len(nums) / 3)

        for n in nums:
            seen[n] += 1

            if seen[n] == cutoff + 1:
                res.append(n)
        
        return res
