class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod = [1] * len(nums)
        suffixprod = [1] * len(nums)
        output = [0] * len(nums)

        for i in range(1, len(nums)):
            prefixprod[i] = nums[i - 1] * prefixprod[i - 1]
            suffixprod[len(nums) - i - 1] = nums[len(nums) - i] * suffixprod[len(nums) - i]
        
        for i in range(len(nums)):
            output[i] = prefixprod[i] * suffixprod[i]

        print(prefixprod)
        print(suffixprod)

        return output

        