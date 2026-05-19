class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        numsLen = len(nums)
        k = len(nums)
        endIndex = numsLen - 1

        for i in range(numsLen):
            if nums[i] == val:
                nums[i] = nums[endIndex]
                endIndex -= 1
                k -= 1
                i -= 1

        return k