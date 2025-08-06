class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without duplicates.   
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item not in '.':
                    s.add(item)


        # Each column must contain the digits 1-9 without duplicates.
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item not in '.':
                    s.add(item)


        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i, j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item not in '.':
                        s.add(item)
        
        return True

        
