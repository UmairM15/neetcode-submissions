from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums:
            if count[n] != 0:
                return True
            count[n] += 1
        return False