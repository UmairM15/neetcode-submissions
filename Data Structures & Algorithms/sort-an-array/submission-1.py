class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        if numsLen <= 1:
            return nums
        mid = int(numsLen / 2)
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))

    def merge(self, left, right):
        i = 0 
        j = 0
        arr = []
        leftLen = len(left)
        rightLen = len(right)

        while i < leftLen and j < rightLen:
            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1

        arr.extend(left[i:])
        arr.extend(right[j:])
        
        return arr