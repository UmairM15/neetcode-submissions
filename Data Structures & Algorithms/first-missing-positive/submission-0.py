class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallestPos = 1
        seen = set()

        for n in nums:
            seen.add(n)

            if n > 0 and n == smallestPos:
                while smallestPos in seen:
                    smallestPos += 1

        return smallestPos