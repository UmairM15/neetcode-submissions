class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        if strs == []:
            return res
        
        for s in strs:
            res = res + str(len(s)) + "#" + s

        print("res:", res)
        return res

    def decode(self, s: str) -> List[str]:
        arr = []
        word = ""
        i = 0
        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1

            i += 1 # skip hash

            for j in range(length):
                word = word + s[i + j]
            arr.append(word)
            word = ""
            i += length

        print("arr:", arr)
        return arr