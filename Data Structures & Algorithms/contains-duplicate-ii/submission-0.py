class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0

        while l < len(nums):
            r = min(len(nums) - 1, l + k)
            for i in range(l + 1, r + 1):
                if nums[l] == nums[i]:
                    return True
            l += 1

        return False