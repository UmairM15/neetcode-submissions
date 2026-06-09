class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums) + 1

        for l in range(len(nums)):
            curSum = 0
            for r in range(l, len(nums)):
                curSum += nums[r]
                if curSum >= target:
                    minLen = min(minLen, r - l + 1)
                    break

        return minLen if minLen != len(nums) + 1 else 0

