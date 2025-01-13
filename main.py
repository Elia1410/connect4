def dropPiece(board: list, column: int, piece: int):
    for i, slot in enumerate(board[column]):
        if slot == 0:
            board[column][i] = piece
            break

def prRed(skk): print("\033[91m{}\033[00m" .format(skk), end="")
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end="")
def prNormal(skk): print("{}".format(skk), end="")

def printBoard(board: list):
    for row in range(6):
        for col in range(7):
            piece = board[col][5-row]
            if piece == 1: printColor = prGreen
            if piece == 2: printColor = prRed
            if piece == 0: printColor = prNormal
            printColor(f"[{piece}]")
        print()
    print("---------------------\n 1  2  3  4  5  6  7")


def checkWin(board: list):
    # vertical win
    for row in range(6-3):
        for col in range(7):
            piece = board[col][row]
            if piece != 0 and board[col][row] == board[col][row+1] == board[col][row+2] == board[col][row+3]:
                return piece

    # horizontal win
    for row in range(6):
        for col in range(7-3):
            piece = board[col][row]
            if piece != 0 and board[col][row] == board[col+1][row] == board[col+2][row] == board[col+3][row]:
                return piece
    
    # diagonal win (left to right)
    for row in range(6-3):
        for col in range(7-3):
            piece = board[col][row]
            if piece != 0 and board[col][row] == board[col+1][row+1] == board[col+2][row+2] == board[col+3][row+3]:
                return piece
    
    # diagonal win (right to left)
    for row in range(3, 6):
        for col in range(7-3):
            piece = board[col][row]
            if piece != 0 and board[col][row] == board[col+1][row-1] == board[col+2][row-2] == board[col+3][row-3]:
                return piece
    # no win
    return 0


def evaluateMove(board: list, move: int):
    """
    returns a higher value the better the move is depending on the state of the board
    """

    boardWeights = [
        [1, 1, 1, 1, 1, 1], 
        [1, 2, 2, 2, 2, 1],
        [2, 2, 3, 3, 2, 1],
        [3, 3, 3, 3, 2, 1],
        [2, 2, 3, 3, 2, 1],
        [1, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    boardCopy = [i.copy() for i in board]
    dropPiece(boardCopy, move, 2)
    weight = 0
    moveRow = 0
    for i in range(6):
        if boardCopy[move][i] == 0:
            moveRow = i-1
            weight = boardWeights[move][moveRow]
            break
    
    # evaluate win state
    winLossEval = 0
    if checkWin(boardCopy) == 2:
        winLossEval = 100
    else:
        for i in range(7):
            tempBoard = [i.copy() for i in boardCopy]
            dropPiece(tempBoard, i, 1)
            if checkWin(tempBoard) == 1:
                winLossEval = -100


    connections = 0

    # eval horizontal
    if move < 6:
        if boardCopy[move+1][moveRow] == 2:
            connections += 1
            if move < 5:
                if boardCopy[move+2][moveRow] == 2:
                    connections += 1

    if move > 0:
        if boardCopy[move-1][moveRow] == 2:
            connections += 1
            if move > 1:
                if boardCopy[move-2][moveRow] == 2:
                    connections += 1
    
    # eval vertical
    if moveRow < 5:
        if boardCopy[move][moveRow+1] == 2:
            connections += 1
            if moveRow < 5:
                if boardCopy[move][moveRow+2] == 2:
                    connections += 1

    if moveRow > 0:
        if boardCopy[move][moveRow-1] == 2:
            connections += 1
            if moveRow > 1:
                if boardCopy[move][moveRow-2] == 2:
                    connections += 1

    # eval diagonally
    if move < 6 and moveRow < 5:
        if boardCopy[move+1][moveRow+1] == 2:
            connections += 1
            if move < 5 and moveRow < 4:
                if boardCopy[move+2][moveRow+2] == 2:
                    connections += 1

    if move > 0 and moveRow > 0:
        if boardCopy[move-1][moveRow-1] == 2:
            connections += 1
            if move > 1 and moveRow > 1:
                if boardCopy[move-2][moveRow-2] == 2:
                    connections += 1

    if move < 6 and moveRow > 0:
        if boardCopy[move+1][moveRow-1] == 2:
            connections += 1
            if move < 5 and moveRow > 1:
                if boardCopy[move+2][moveRow-2] == 2:
                    connections += 1

    if move > 0 and moveRow < 5:
        if boardCopy[move-1][moveRow+1] == 2:
            connections += 1
            if move > 1 and moveRow < 4:
                if boardCopy[move-2][moveRow+2] == 2:
                    connections += 1

    return connections + weight + winLossEval

def getBestMove(board: list):
    besteval = 0
    bestMove = 0
    for i in range(7):
        currentEval = evaluateMove(board, i)
        if currentEval > besteval:
            if board[i][-1] == 0:
                besteval = currentEval
                bestMove = i
    return bestMove

    

###### GAME LOOP ######

b = [
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

running = True
from os import system as sys
def clear():
    _ = sys('cls')



while running:
    clear()
    printBoard(b)

    userInput = int(input("your turn (1-7): "))-1
    
    if b[userInput][-1] == 0:
        dropPiece(b, userInput, 1)

    if checkWin(b) == 1:
        running = False
    else:
        dropPiece(b, getBestMove(b), 2)
        if checkWin(b) == 2:
            running = False

clear()
printBoard(b)
winner = checkWin(b)
if winner != 0:
    if winner == 1: printColor = prGreen
    if winner == 2: printColor = prRed
    printColor(f"Player{winner} wins!")
    running = False