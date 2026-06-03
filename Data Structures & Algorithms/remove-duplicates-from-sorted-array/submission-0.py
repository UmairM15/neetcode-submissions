class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()

        i, j = 0, 0

        while j < len(nums):
            if nums[j] not in seen:
                nums[i] = nums[j]
                seen.add(nums[i])
                i += 1
                k += 1
            j += 1
        
        return k