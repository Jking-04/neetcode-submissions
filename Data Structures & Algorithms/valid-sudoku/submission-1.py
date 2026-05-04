class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows=   [[] for _ in range(9)]
        columns=[[] for _ in range(9)]
        boxes=  [[] for _ in range(9)]

        for y in range(9):
            for x in range(9):
                value=board[y][x]

                if value.isalnum():

                    if value in rows[y]:
                        return False
                    else:
                        rows[y].append(value)

                    if value in columns[x]:
                        return False
                    else:
                        columns[x].append(value)

                    box = (x//3)+3*(y//3)
                    if value in boxes[box]:
                        return False
                    else:
                        boxes[box].append(value)

        return True
