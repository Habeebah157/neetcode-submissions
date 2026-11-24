class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLUMNS = len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLUMNS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
    

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                if (board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLUMNS-1])): 
                    print("Her")
                    capture(r, c)
            
        
        # for r in range(ROWS): 
        #     for c in range(COLUMNS): 
        #         if (board[r][c] == "O" and (r in [0, ROWS] or c in [0, COLUMNS])): 
        #             print("HERE")
        #             capture(r, c)  
        #             print("here",board)


        for r in range(ROWS): 
            for c in range(COLUMNS): 
                if board[r][c] == "O": 
                    board[r][c] = "X"
        
        for r in range(ROWS): 
            for c in range(COLUMNS): 
                if board[r][c] == "T": 
                    board[r][c] = "O"
        