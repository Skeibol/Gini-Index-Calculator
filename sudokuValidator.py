import numpy as np

def valid_solution(board):
    board = np.array(board)
    state=True
    c=0
    while c<9:
        a = sum(sum(board[c:c+3,c:c+3]))
        if (sum(sum(board[c:c+3,c:c+3])))!=45:
            state=False
        c+=3
    
    zbroj = 0
    c=0
    for i in board[0]:
        if sum(board[:,c])!=45:
            state=False
        if sum(board[c,:])!=45:
            state=False
        c+=1
    
    return state
    
        
    
    
board =                         [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(valid_solution(board))
valid_solution(board)