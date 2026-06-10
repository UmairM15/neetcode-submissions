class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for curOp in operations:
            if curOp == "+" and len(rec) > 1:
                newScore = rec[-1] + rec[-2]
                rec.append(newScore)
            elif curOp == "D" and len(rec) > 0:
                rec.append(rec[-1] * 2)
            elif curOp == "C" and len(rec) > 0:
                rec.pop()
            else:
                rec.append(int(curOp))
        return sum(rec)
