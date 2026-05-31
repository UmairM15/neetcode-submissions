from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        prefix = [0] * len(nums)
        prefCnt = defaultdict(int)
        res = 0

        prefCnt[0] = 1

        for n in nums:
            prefixsum += n
            res += prefCnt[prefixsum - k]
            prefCnt[prefixsum] += 1

        return res