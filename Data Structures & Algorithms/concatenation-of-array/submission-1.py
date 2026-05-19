class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        ans = [0] * (2 * numLen)
        for i in range(numLen):
            ans[i] = nums[i]
            ans[i + numLen] = nums[i]

        return ans
        