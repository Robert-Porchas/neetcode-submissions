class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxHash = {}
        colHash = {num: {} for num in range(0, 9)} 
        # will be one hash for all columns
        for i in range(len(board)):
            rowHash = {}
            for j in range(len(board[i])):
                preDigit = board[i][j] # now can process on this number
                if preDigit.isdigit() == False:
                    continue
                currentDigit = int(preDigit)
                # check if its in the row, then add it
                if currentDigit in rowHash:
                    return False
                rowHash[currentDigit] = True
                # check if its in the column, then add it
                if currentDigit in colHash[j]:
                    return False
                colHash[j][currentDigit] = True
                # check if its in the box, then add it
                # first make sure that the hash is initialized
                if (i//3, j//3) not in boxHash:
                    boxHash[(i//3, j//3)] = {}
                if currentDigit in boxHash[(i//3, j//3)]:
                    return False
                boxHash[(i//3, j//3)][currentDigit] = True
        return True