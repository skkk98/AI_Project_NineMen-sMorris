import sys
from NineMensMorrisGenerators import *


def ABOpening(board, color, depth, alpha, beta):
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
    else:
        flippedboard = boardflip(board)
        boardpositions = GenerateMovesOpening(flippedboard)
        for number in range(0, len(boardpositions)):
            boardpositions[number] = boardflip(boardpositions[number])

    for position in boardpositions:
        if color == 'W':
            newboard, nodes, newvalue = ABOpening(list(position), 'B', depth - 1, alpha, beta)
            nodecount += nodes
            if newvalue > alpha:
                alpha = newvalue
                bestboard = position
        else:
            newboard, nodes, newvalue = ABOpening(list(position), 'W', depth - 1, alpha, beta)
            nodecount += nodes
            if newvalue < beta:
                beta = newvalue
                bestboard = position
        if alpha >= beta:
            break

    if color == 'W':
        value = alpha
    else:
        value = beta
    return bestboard, nodecount, value


if __name__ == '__main__':
    readfile = open(sys.argv[1], "r")
    input_board = readfile.readline()
    print("Input Board Position: " + input_board)
    input_board = list(input_board)
    nextboard, poscount, val = ABOpening(input_board, 'W', int(sys.argv[3]), -1000000, 1000000)
    print("Output Board Position: " + "".join(nextboard))
    print("Positions Evaluated by static estimation: " + str(poscount))
    print("Minimax estimate: " + str(val))
    writefile = open(sys.argv[2], "w")
    writefile.write("".join(nextboard))
