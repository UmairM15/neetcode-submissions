class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = j = 0

        while j < len(nums):
            if j > 0 and nums[j] == nums[j - 1]:
                j += 1
                continue
            nums[i] = nums[j]
            i += 1
            j += 1
            k += 1

        return k