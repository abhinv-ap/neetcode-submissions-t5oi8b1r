class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def all_good(unit):
            nums=[i for i in unit if i!='.']
            return len(nums)==len(set(nums))
        
        for i in board:
            if not all_good(i):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if not all_good(col):
                return False
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                box=[]
                for i in range(3):
                    for j in range(3):
                        box.append(board[r+i][c+j])
                
                if not all_good(box):
                    return False
        return True
            
        
        
            
        