class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        j = curSum = 0
        for curOp in operations:
            if curOp == "+":
                newScore = rec[j - 1] + rec[j - 2]
                curSum += newScore
                rec.append(newScore)
                j += 1
            elif curOp == "D":
                rec.append(rec[j - 1] * 2)
                curSum += rec[j]
                j += 1
            elif curOp == "C":
                curSum -= rec[j - 1]
                rec.pop()
                j -= 1
            else:
                rec.append(int(curOp))
                curSum += int(curOp)
                j += 1
        return curSum
