class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        ans = [None] * (numLen * 2)
        for i in range(numLen):
            ans[i] = nums[i]
            ans[i + numLen] = nums[i]

        return ans
        