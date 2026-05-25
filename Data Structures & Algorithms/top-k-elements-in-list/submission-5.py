from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        numsLen = len(nums)

        for n in nums:
            count[n] += 1

        freq = [[] for _ in range(numsLen + 1)]
        for n in count:
            (freq[count[n]]).append(n)

        arr = []
        i = numsLen
        while k > 0:
            if freq[i] != []:
                for n in freq[i]:
                    print("n:", n)
                    arr.append(n)
                    k -= 1
            i -= 1

        return arr