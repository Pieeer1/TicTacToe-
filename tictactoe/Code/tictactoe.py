#Mason Adams
#Cs 482
#Project 1
import sys
import fileinput
import random


gameBoard = []
huplayer = str(1)
aiplayer = str(-1)
huscore= []
aiscore = []
moves = []


sys.setrecursionlimit(10000)
random.seed

def save_board():
    filename = sys.argv[2]

    outFile = open(filename, 'w')

    counter = 0
    for char in gameBoard:
        counter=counter+1
        outFile.write(char)
        outFile.write("    ") 
        if counter % 3 ==0:
            outFile.write("\n")

def load_board():
    filename = sys.argv[1]


    #Apply Input File to GameBoard List
    with open(filename,'r') as file:
        for line in file:
            for word in line.split():
                gameBoard.append(word)

    #for item in gameBoard:
    #   item = int(item)

# win_score
#
#gives +10 or -10 values to moves in certain positions depending on if it ends in a win position
def win_score(newBoard, player):


    emptycells = []
    emptycells = [i for i, value in enumerate(newBoard)if value =='0']
    if(winning_move(newBoard, huplayer)):
        return -10
    elif(winning_move(newBoard, aiplayer)):
        return 10 
    else:
        return 0

# minimax
#
# Uses a minimax function by randomly attributing winning values and recycling moves between players to determine the next best possible move
def minimax(newBoard, player):
    rCounter = int(0)

    #determines empty cells
    emptycells = []
    emptycells = [i for i, value in enumerate(newBoard)if value =='0']
    #print(emptycells)
    updatedBoard = newBoard
    #print(win_score(updatedBoard,player))
    if(len(emptycells)>0):
        bestMove = emptycells[0]
    emptySpace=0
    if win_score(newBoard,player) == 0:
        while emptySpace < len(emptycells):
            if(len(emptycells)>0):
                updatedBoard[emptycells[emptySpace]]=player

            #print(updatedBoard)

            #Adds scores to the determined score arrays

            huscore.append(0)
            aiscore.append(0)
            huscore[emptySpace] = (win_score(updatedBoard,player) +huscore[emptySpace])
            aiscore[emptySpace] = (win_score(updatedBoard,player) +aiscore[emptySpace])


            # uses recursion to sift through all possible future moves.

            if(player == aiplayer):
                moves.append(minimax(updatedBoard,huplayer))
            if(player == huplayer):
                moves.append(minimax(updatedBoard,aiplayer))

            #determines best move based on scores


            emptySpace+=1
            if(player == aiplayer):
                bestScore = -10000
                for count in moves:
                    aiscore.append(0)
                    if aiscore[count] > bestScore:
                        bestMove = emptycells[count]
                        return bestMove
            else:
                bestScore = 10000
                for count in moves:
                    huscore.append(0)
                    if huscore[count] < bestScore:
                        bestMove = emptycells[count]
                        return bestMove
            #return 0

    return 0




# winning_move
#
# determines, given the board state, if there is a winning move made
def winning_move(board, player):


    temp = True
    if (str(board[0]) == player and str(board[1]) == player and str(board[2]) == player) or(str(board[3]) == player and str(board[4]) == player and str(board[5]) == player) or(str(board[6]) == player and str(board[7]) == player and str(board[8]) == player) or(str(board[0]) == player and str(board[3]) == player and str(board[6]) == player) or(str(board[1]) == player and str(board[4]) == player and str(board[7]) == player) or(str(board[2]) == player and str(board[5]) == player and str(board[8]) == player) or(str(board[0]) == player and str(board[4]) == player and str(board[8]) == player) or(str(board[2]) == player and str(board[4]) == player and str(board[6]) == player):
        temp  = True
    else:
       temp = False
    return temp

    


# make_move
#
# calls a minimax function on a value that saves the location  of the most valuable move
def make_move():

    final_move = 0
    final_move = minimax(gameBoard,aiplayer)
    #print(moves)
    return final_move



#   main
#
#   holds functions, actually makes move, and loads/saves the board
def main():
    load_board()

    #print(str(gameBoard) + "\n\n")
    movePlacement = make_move()

    print("The AI moves to cell :"+str(movePlacement))

    gameBoard.clear()
    load_board()
    gameBoard[movePlacement]=aiplayer

    save_board()

    


if __name__ == "__main__":
    main()