class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row_len = len(board)
        col_len = len(board[0])
        visited=set()
        def backtrack(row,col,index):
            # for the bounds checking
            
            if row < 0 or row >= row_len:
                return False
           
            if col < 0 or col >= col_len:
                return False
            
            if (row,col) in visited:
                return False

            if board[row][col] != word[index]:
                return False
            
            if index == len(word)-1:
                return True
            
            visited.add((row,col))

            found=(
                backtrack(row+1,col,index+1) or
                backtrack(row-1,col,index+1) or
                backtrack(row,col+1,index+1) or
                backtrack(row,col-1,index+1)
            )
            visited.remove((row,col))
            return found

        for row in range(row_len):
            for col in range(col_len):
                if backtrack(row,col,0):
                    return True
            
        return False
            

        