def GenerateMovesOpening(board):
    return GenerateAdd(board)


def GenerateMovesMidgameEndgame(board):
    whitecount = 0
    for location in range(0, len(board)):
        if board[location] == 'W':
            whitecount += 1

    if whitecount == 3:
        return GenerateHopping(board)
    else:
        return GenerateMove(board)


def GenerateAdd(board):
    boardslist = []
    for location in range(0, len(board)):
        if board[location] == 'x':
            newboard = list(board)
            newboard[location] = 'W'
            if closeMill(location, newboard):
                boardslist = GenerateRemove(newboard, boardslist)
            else:
                boardslist.append(newboard)
    return boardslist


def GenerateRemove(board, boardlist):
    flag = 0
    for location in range(0, len(board)):
        if board[location] == 'B':
            if not closeMill(location, board):
                flag = 1
                newboard = list(board)
                newboard[location] = 'x'  # removed opponents piece
                boardlist.append(newboard)
    if flag == 1:  # Removed different black pieces
        return boardlist
    else:  # no black pieces to remove(all B are part of mills)
        boardlist.append(board)
        return boardlist


def GenerateMove(board):
    boardslist = []
    for location in range(0, len(board)):
        if board[location] == 'W':
            n = neighbors(location)
            for neighbor in n:
                if board[neighbor] == 'x':
                    newboard = list(board)
                    newboard[location] = 'x'
                    newboard[neighbor] = 'W'
                    if closeMill(neighbor, newboard):
                        boardslist = GenerateRemove(newboard, boardslist)
                    else:
                        boardslist.append(newboard)
    return boardslist


def GenerateHopping(board):
    boardslist = []
    for location1 in range(0, len(board)):
        if board[location1] == 'W':
            for location2 in range(0, len(board)):
                if board[location2] == 'x':
                    newboard = list(board)
                    newboard[location1] = 'x'
                    newboard[location2] = 'W'
                    if closeMill(location2, newboard):
                        boardslist = GenerateRemove(newboard, boardslist)
                    else:
                        boardslist.append(newboard)
    return boardslist


def closeMill(location, board):
    color = board[location]
    if location == 0:
        if (board[2] == color and board[4] == color) or (board[6] == color and board[18] == color):
            return True
        else:
            return False
    elif location == 1:
        if (board[3] == color and board[5] == color) or (board[11] == color and board[20] == color):
            return True
        else:
            return False
    elif location == 2:
        if (board[0] == color and board[4] == color) or (board[7] == color and board[15] == color):
            return True
        else:
            return False
    elif location == 3:
        if (board[1] == color and board[5] == color) or (board[10] == color and board[17] == color):
            return True
        else:
            return False
    elif location == 4:
        if (board[0] == color and board[2] == color) or (board[8] == color and board[12] == color):
            return True
        else:
            return False
    elif location == 5:
        if (board[1] == color and board[3] == color) or (board[9] == color and board[14] == color):
            return True
        else:
            return False
    elif location == 6:
        if (board[0] == color and board[18] == color) or (board[7] == color and board[8] == color):
            return True
        else:
            return False
    elif location == 7:
        if (board[2] == color and board[15] == color) or (board[6] == color and board[8] == color):
            return True
        else:
            return False
    elif location == 8:
        if (board[4] == color and board[12] == color) or (board[6] == color and board[7] == color):
            return True
        else:
            return False
    elif location == 9:
        if (board[5] == color and board[14] == color) or (board[10] == color and board[11] == color):
            return True
        else:
            return False
    elif location == 10:
        if (board[3] == color and board[17] == color) or (board[9] == color and board[11] == color):
            return True
        else:
            return False
    elif location == 11:
        if (board[1] == color and board[20] == color) or (board[9] == color and board[10] == color):
            return True
        else:
            return False
    elif location == 12:
        if (board[4] == color and board[8] == color) or (board[13] == color and board[14] == color) \
                or (board[15] == color and board[18] == color):
            return True
        else:
            return False
    elif location == 13:
        if (board[12] == color and board[14] == color) or (board[16] == color and board[19] == color):
            return True
        else:
            return False
    elif location == 14:
        if (board[5] == color and board[9] == color) or (board[12] == color and board[13] == color) \
                or (board[17] == color and board[20] == color):
            return True
        else:
            return False
    elif location == 15:
        if (board[2] == color and board[7] == color) or (board[12] == color and board[18] == color) \
                or (board[16] == color and board[17] == color):
            return True
        else:
            return False
    elif location == 16:
        if (board[13] == color and board[19] == color) or (board[15] == color and board[17] == color):
            return True
        else:
            return False
    elif location == 17:
        if (board[3] == color and board[10] == color) or (board[14] == color and board[20] == color) \
                or (board[15] == color and board[16] == color):
            return True
        else:
            return False
    elif location == 18:
        if (board[0] == color and board[6] == color) or (board[12] == color and board[15] == color) \
                or (board[19] == color and board[20] == color):
            return True
        else:
            return False
    elif location == 19:
        if (board[13] == color and board[16] == color) or (board[18] == color and board[20] == color):
            return True
        else:
            return False
    elif location == 20:
        if (board[1] == color and board[11] == color) or (board[14] == color and board[17] == color) \
                or (board[18] == color and board[19] == color):
            return True
        else:
            return False
    else:
        return False


def neighbors(location):
    neighborslist = []
    if location == 0:
        neighborslist = [1, 2, 6]
    elif location == 1:
        neighborslist = [0, 3, 11]
    elif location == 2:
        neighborslist = [0, 3, 4, 7]
    elif location == 3:
        neighborslist = [1, 2, 5, 10]
    elif location == 4:
        neighborslist = [2, 5, 8]
    elif location == 5:
        neighborslist = [4, 3, 9]
    elif location == 6:
        neighborslist = [0, 7, 18]
    elif location == 7:
        neighborslist = [2, 6, 8, 15]
    elif location == 8:
        neighborslist = [4, 7, 12]
    elif location == 9:
        neighborslist = [5, 10, 14]
    elif location == 10:
        neighborslist = [3, 9, 11, 17]
    elif location == 11:
        neighborslist = [1, 10, 20]
    elif location == 12:
        neighborslist = [8, 13, 15]
    elif location == 13:
        neighborslist = [12, 14, 16]
    elif location == 14:
        neighborslist = [9, 13, 17]
    elif location == 15:
        neighborslist = [7, 12, 16, 18]
    elif location == 16:
        neighborslist = [13, 15, 17, 19]
    elif location == 17:
        neighborslist = [10, 14, 16, 20]
    elif location == 18:
        neighborslist = [6, 15, 19]
    elif location == 19:
        neighborslist = [16, 18, 20]
    elif location == 20:
        neighborslist = [11, 17, 19]

    return neighborslist


def staticEstimationOpening(board):
    whitecount = 0
    blackcount = 0

    for location in range(0, len(board)):
        if board[location] == 'W':
            whitecount += 1
        elif board[location] == 'B':
            blackcount += 1

    return whitecount - blackcount


def staticEstimationMidgameEndgame(board):
    whitecount = 0
    blackcount = 0
    # To get blackmoves, we flip the board and then pass the board to GenerateMovesMidgameEndgame function
    newboard = boardflip(list(board))
    blackboardpositions = GenerateMovesMidgameEndgame(newboard)  # GenerateBlackMovesMidgameEndgame(board)
    #print(blackboardpositions)
    possibleblackmoves = len(blackboardpositions)

    for location in range(0, len(board)):
        if board[location] == 'W':
            whitecount += 1
        elif board[location] == 'B':
            blackcount += 1

    if blackcount <= 2:
        return 10000  # White wins!
    elif whitecount <= 2:
        return -10000  # Black wins!
    elif possibleblackmoves == 0:
        return 10000  # White wins! No possible moves for Black
    else:
        return 1000 * (whitecount - blackcount) - possibleblackmoves


def boardflip(board):
    for location in range(0, len(board)):
        if board[location] == 'W':
            board[location] = 'B'
        elif board[location] == 'B':
            board[location] = 'W'

    return board
# def GenerateBlackMovesMidgameEndgame(board):
#     blackcount = 0
#     for location in range(0, len(board)):
#         if board[location] == 'B':
#             blackcount += 1
#
#     if blackcount == 3:
#         return GenerateHopping(board)
#     else:
#         return GenerateHopping(board)
