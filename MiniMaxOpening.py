import sys
from NineMensMorrisGenerators import *


def MiniMaxOpening(board, color, depth):
    if depth == 0:
        nodes = 1
        value = staticEstimationOpening(board)
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
            newboard, nodes, newvalue = MiniMaxOpening(list(position), 'B', depth - 1)
            nodecount += nodes
            if newvalue > value:
                value = newvalue
                bestboard = position
        else:
            newboard, nodes, newvalue = MiniMaxOpening(list(position), 'W', depth - 1)
            nodecount += nodes
            if newvalue < value:
                value = newvalue
                bestboard = position

    return bestboard, nodecount, value


if __name__ == '__main__':
    readfile = open(sys.argv[1], "r")
    input_board = readfile.readline()
    print("Input Board Position: " + input_board)
    input_board = list(input_board)
    nextboard, poscount, val = MiniMaxOpening(input_board, 'W', int(sys.argv[3]))
    print("Output Board Position: " + "".join(nextboard))
    print("Positions Evaluated by static estimation: " + str(poscount))
    print("Minimax estimate: " + str(val))
    writefile = open(sys.argv[2], "w")
    writefile.write("".join(nextboard))
