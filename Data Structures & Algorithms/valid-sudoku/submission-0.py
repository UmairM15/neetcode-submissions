from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxIndex = -1
        boxSet, rowSet, colSet = defaultdict(list), defaultdict(list), defaultdict(list)
        ROW = len(board)
        COL = len(board[0])

        for rowIndex in range(ROW):
            if rowIndex % 3 != 0:
                boxIndex -= 3
            for colIndex in range(COL):
                if colIndex % 3 == 0:
                    boxIndex += 1

                if (num := board[rowIndex][colIndex]) != ".":
                    if num in boxSet[boxIndex]:
                        return False
                    else:
                        boxSet[boxIndex].append(num)

                    if num in rowSet[rowIndex]:
                        return False
                    else:
                        rowSet[rowIndex].append(num)

                    if num in colSet[colIndex]:
                        return False
                    else:
                        colSet[colIndex].append(num)

        return True
