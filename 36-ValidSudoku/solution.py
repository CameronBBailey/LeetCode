class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validationListRow = []
        validationListC = []
        for i in range(9):
            for j in board[i]:
                if j in validationListRow:
                    return False
                elif j != ".":
                    validationListRow.append(j)
            validationListRow = []
            for k in board:
                if k[i] in validationListC:
                    return False
                elif k[i] != ".":
                    validationListC.append(k[i])
            validationListC = []
            boxColumn = (i) // 3
            boxRow = (i % 3)
            print(f" I = {i}")
            print(f"boxColumn {boxColumn}")
            print(f"boxRow = {boxRow}")
            # print(board[slice(boxColumn * 3, (boxColumn * 3) +2)][slice(boxRow, boxRow+2)])
            for p in board[slice(boxColumn * 3, (boxColumn * 3) +3)]:
                for h in p[slice(boxRow*3, (boxRow *3)+3)]:
                    print(f"h = {h}")
                    if h in validationListC:
                        return False
                    elif h != ".":
                        validationListC.append(h)
            validationListC = []
                
        
        return True
