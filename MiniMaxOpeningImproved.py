import sys
from NineMensMorrisGenerators import *


def MiniMaxOpeningImproved(board, color, depth):
    if depth == 0:
        nodes = 1
        value = staticEstimationOpeningImproved(board)
        return board, nodes, value

    boardpositions = []
    value = 0
    nodecount = 0
    bestboard = []

    if color == 'W':
        boardpositions = GenerateMovesOpening(board)
        value = -1000000
    else:
        flippedboard = boardflip(board)
        boardpositions = GenerateMovesOpening(flippedboard)
        for number in range(0, len(boardpositions)):
            boardpositions[number] = boardflip(boardpositions[number])
        value = 1000000

    for position in boardpositions:
        if color == 'W':
            newboard, nodes, newvalue = MiniMaxOpeningImproved(list(position), 'B', depth - 1)
            nodecount += nodes
            if newvalue > value:
                value = newvalue
                bestboard = position
        else:
            newboard, nodes, newvalue = MiniMaxOpeningImproved(list(position), 'W', depth - 1)
            nodecount += nodes
            if newvalue < value:
                value = newvalue
                bestboard = position

    return bestboard, nodecount, value


def staticEstimationOpeningImproved(board):
    whitecount = 0
    blackcount = 0

    for location in range(0, len(board)):
        if board[location] == 'W':
            whitecount += 1
        elif board[location] == 'B':
            blackcount += 1

    return 10 * (whitecount - blackcount) + 100 * (getPossibleMills(board))


def getPossibleMills(board):
    total_mills = 0
    for location in range(0, len(board)):
        if board[location] == 'x':
            new_board = list(board)
            new_board[location] = 'W'
            if closeMill(location, new_board):
                total_mills += 1
    return total_mills


if __name__ == '__main__':
    readfile = open(sys.argv[1], "r")
    input_board = readfile.readline()
    print("Input Board Position: " + input_board)
    input_board = list(input_board)
    nextboard, poscount, val = MiniMaxOpeningImproved(input_board, 'W', int(sys.argv[3]))
    print("Output Board Position: " + "".join(nextboard))
    print("Positions Evaluated by static estimation: " + str(poscount))
    print("Minimax estimate: " + str(val))
    writefile = open(sys.argv[2], "w")
    writefile.write("".join(nextboard))
