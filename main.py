board = [[0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]
        ]



def dropPiece(board: list, column: int, piece: int):
    for i, slot in enumerate(board[column]):
        if slot == 0:
            board[column][i] = piece
            break


def printBoard(board):
    for i, c in enumerate(board):
        print(f"{i}: {c}")


def checkWin(board: list):
    # vertical win
    player1 = 0
    player2 = 0
    for i, slot in enumerate(board):
        if slot == 1:
            player1 += 1
            player2 = 0
        elif slot == 2: 
            player2 += 1
            player1 = 0
        elif slot == 0:
            player1 = 0
            player2 = 0
    if player1 > 3: return 1
    if player2 > 3: return 2

    # horizontal win
    player1 = 0
    player2 = 0
    

    # diagonal win