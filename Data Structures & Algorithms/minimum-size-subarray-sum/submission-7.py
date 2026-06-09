class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curSum = 0
        minWindow = len(nums) + 1
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minWindow = min(minWindow, r - l + 1)
                curSum -= nums[l]
                l += 1
        return minWindow if minWindow != len(nums) + 1 else 0
            