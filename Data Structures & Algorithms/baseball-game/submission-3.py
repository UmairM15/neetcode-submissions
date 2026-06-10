class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for curOp in operations:
            if curOp == "+":
                newScore = rec[-1] + rec[-2]
                rec.append(newScore)
            elif curOp == "D":
                rec.append(rec[-1] * 2)
            elif curOp == "C":
                rec.pop()
            else:
                rec.append(int(curOp))
        return sum(rec)
