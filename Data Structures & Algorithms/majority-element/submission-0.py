from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        majorityCutoff = len(nums) / 2

        for n in nums:
            seen[n] += 1

            if seen[n] > majorityCutoff:
                return n
            