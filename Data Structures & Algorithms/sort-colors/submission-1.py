from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        val = 0
        for i in range(len(nums)):
            while count[val] == 0:
                val += 1
            nums[i] = val
            count[val] -= 1