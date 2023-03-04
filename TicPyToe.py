import random

def drawBoard(TicTacToe):
    print('')
    print('  A   B   C')
    for rowNumber in range(0,3):
        row = str(rowNumber+1) + ' ' + TicTacToe[rowNumber][0] + ' | ' + TicTacToe[rowNumber][1] + ' | ' + TicTacToe[rowNumber][2]
        print(row)
    print('')

def userMove(TicTacToe):
    move = input("Enter your move: ")
    try:
        x = move[0]
        y = move[1]
        y = int(y) - 1

        if x == 'A' or x == 'a':
            x = 0

        if x == 'B' or x == 'b':
            x = 1

        if x == 'C' or x == 'c':
            x = 2

        if TicTacToe[y][x] == ' ':
            TicTacToe[y][x] = 'X'
        else:
            print("Field already filled! Try again")
            userMove(TicTacToe)
    except:
        print("Illegal move! Try again!")
        userMove(TicTacToe)

def botMove(TicTacToe):
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if TicTacToe[y][x] == ' ' and hasEmptyFields(TicTacToe) == True:
            TicTacToe[y][x] = 'O'
        else:
            botMove(TicTacToe)

def hasEmptyFields(TicTacToe):
    for i in range(0,3):
        for j in range(0,3):
            if TicTacToe[i][j] == ' ':
                return True
    return False

def isWon(TicTacToe):
    if (TicTacToe[0][0] == 'X' and TicTacToe[0][1] == 'X' and TicTacToe[0][2] == 'X'
    ) or (TicTacToe[1][0] == 'X' and TicTacToe[1][1] == 'X' and TicTacToe[1][2] == 'X'
    ) or (TicTacToe[2][0] == 'X' and TicTacToe[2][1] == 'X' and TicTacToe[2][2] == 'X'

    ) or (TicTacToe[0][0] == 'X' and TicTacToe[1][0] == 'X' and TicTacToe[2][0] == 'X'
    ) or (TicTacToe[0][1] == 'X' and TicTacToe[1][1] == 'X' and TicTacToe[2][1] == 'X'
    ) or (TicTacToe[0][2] == 'X' and TicTacToe[1][2] == 'X' and TicTacToe[2][2] == 'X'

    ) or (TicTacToe[0][0] == 'X' and TicTacToe[1][1] == 'X' and TicTacToe[2][2] == 'X'
    ) or (TicTacToe[2][0] == 'X' and TicTacToe[1][1] == 'X' and TicTacToe[0][2] == 'X'):
        print("User has won!")
        return True

    elif (TicTacToe[0][0] == 'O' and TicTacToe[0][1] == 'O' and TicTacToe[0][2] == 'O'
    ) or (TicTacToe[1][0] == 'O' and TicTacToe[1][1] == 'O' and TicTacToe[1][2] == 'O'
    ) or (TicTacToe[2][0] == 'O' and TicTacToe[2][1] == 'O' and TicTacToe[2][2] == 'O'

    ) or (TicTacToe[0][0] == 'O' and TicTacToe[1][0] == 'O' and TicTacToe[2][0] == 'O'
    ) or (TicTacToe[0][1] == 'O' and TicTacToe[1][1] == 'O' and TicTacToe[2][1] == 'O'
    ) or (TicTacToe[0][2] == 'O' and TicTacToe[1][2] == 'O' and TicTacToe[2][2] == 'O'

    ) or (TicTacToe[0][0] == 'O' and TicTacToe[1][1] == 'O' and TicTacToe[2][2] == 'O'
    ) or (TicTacToe[2][0] == 'O' and TicTacToe[1][1] == 'O' and TicTacToe[0][2] == 'O'):
        print("Computer has won!")
        return True

    else:
        return False

if __name__ == "__main__":

    TicTacToe = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    drawBoard(TicTacToe)

    while True:

        if hasEmptyFields(TicTacToe) == True:
            userMove(TicTacToe)
        else:
            drawBoard(TicTacToe)
            print('Draw!')
            break

        if hasEmptyFields(TicTacToe) == True:
            botMove(TicTacToe)
        else:
            drawBoard(TicTacToe)
            print('Draw!')
            break

        drawBoard(TicTacToe)

        if isWon(TicTacToe) == True:
            break