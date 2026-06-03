class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            compl = target - numbers[i]

            while compl < numbers[j]:
                j -= 1
            if compl == numbers[j]:
                return [i + 1, j + 1]
            i += 1