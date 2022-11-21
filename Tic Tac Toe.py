def mainGame():
    import random
    import time
    import sys
    import os

    #---------------------------------------------Game Board and Global Variables---------------------------------------
    #A list variable to be used for passing into the visual print functions. This list starts off as hyphens, and will be changed
    #by other other functions as the game continues by the playerInput() function. A LIST is important as we need to reference variable by index number.
    global board
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

    global winner
    winner = None
    global instructions
    instructions = "Enter an Integer: 1 - 9 to place your token into a box containing ' - '\n(1 = top-left, 9 = bottom-right)"


    #---------------------------------------------Misktake Counter and Reply Message-------------------------------------
    #a function to track player non-compliance and adjust return messages accordingly.
    def mistakeCount():
        global mistakes
        global reply
        try:
            mistakes
        except:
            mistakes = 1
        else:
            mistakes += 1

        if mistakes <=3:
            reply = "Try Again!"
        elif 3 < mistakes <= 5:
            reply = "It's Ok. Take your time."
        elif mistakes == 6:
            reply = "The isntructions are written below."
        elif mistakes == 7:
            reply = "Are you reading the directions?"
        elif mistakes == 8:
            reply = "I don't care what they say. I believe you CAN read!"
        elif mistakes == 9:
            reply = "Seriously, read the directions. It's not hard. They're two lines down."
        elif mistakes == 10:
            reply = "Bruh, It's Tic-Tac-Toe. X's...O's...Lines...Simple Words...etc."
        elif mistakes == 11:
            reply = "Wrangle it in, Cowpoke! It's time to focus up."
        elif mistakes == 12:
            reply = "I think you're doing this on purpose!"
        elif mistakes == 13:
            reply = "I'm sad, tired, and running out of conditionals."
        elif mistakes == 14:
            reply = "FIGURE IT OUT, MATE!"
        elif mistakes == 15:
            reply = "Alright, now you're trying to be quarrelsome."
        elif mistakes > 15:
            reply = ":c"

    #--------------------------------------1-Player or 2-Player Game Selection-------------------------------------------
    def playerNo():
        global players
        while True:
            players = input(f"How many players? 1 or 2?\n")
            if players == "1" or "n" in players or "N" in players:
                players = 1
                os.system('cls')
                break
            elif players == "2" or "t" in players or "T" in players:
                players = 2
                os.system('cls')
                break
            else:
                mistakeCount()
                print(f"\nType the number of players playing:\n Your choices are: \"1\" or \"2\"?\n{reply}\n")

    #--------------------------------------Assign Player & Computer Tokens-----------------------------------------------
    #Function for assigning variable for player token (Xs or Os) and computer token based on user input

    def chooseToken():
        global p1Token
        global p2Token
        global cToken
        global p1Name
        global p2Name
        p1Name = input(f"\nPlayer 1, what's your name?\n")
        while True:
            pchoose = input(f"\n{p1Name}, would you like to play as X or O?\n")
            if "X" in pchoose or "x" in pchoose:
                p1Token = "X"
                cToken = "O"
                if players == 2:
                    p2Token = "O"
                    p2Name = input(f"\nPlayer 2, what's your name?\n")
                    print(f"\n{p2Name}, you'll be playing O's.")
                break
            elif "o" in pchoose or "O" in pchoose or "0" in pchoose:
                p1Token = "O"
                cToken = "X"
                if players == 2:
                    p2Token = "X"
                    p2Name = input(f"\nPlayer 2, what's your name?\n")
                    print(f"\n{p2Name}, you'll be playing X's.")
                break
            else:
                mistakeCount()
                print(f"\n{p1Name}, that's not an X or an O...\nType X or O to play.\n{reply}")

    #--------------------------------------Assign Computer Difficulty-----------------------------------------------
    #Sets variable to choose random computer moves or computer moves based on "next-move win conditions"
    def setDifficutly():
        global compDifficulty
        while True:
            os.system('cls')
            compDifficulty = input(f"\nSelect Difficulty: Easy / Medium / Hard\n")
            if "h" in compDifficulty or "H" in compDifficulty: 
                compDifficulty = "hard"
                break
            elif "s" in compDifficulty or "y" in compDifficulty.lower():
                compDifficulty = "easy"
                break
            elif "m" in compDifficulty or "M" in compDifficulty:
                compDifficulty = "medium"
                break
            else:
                mistakeCount()
                print(f"\nPlease type either \"easy\", \"Medium\", or \"hard\" into the terminal and press \"enter\".\n{reply}\n")

    #---------------------------------------------Print the Game Board to the Terminal--------------------------------
    #The function which takes the list variable "board" and prints values to the terminal
    #the list indices of the board variable start at 0 
    def printBoard(board):
        print(f"\n{instructions}")
        print("\n")
        print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
        print(" -------------")
        print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
        print(" -------------")
        print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

    #---------------------------------------------Player Input Function-------------------------------------------------
    #Take player input, check the validity of that input, and change the "board" list variable as necessary.
    #input will need to be subtracted by 1 as list indices start at 0
    def player1Input(board):
        while True:
            try:
                inp = int(input(f"{p1Name}, Enter an Integer 1-9:\n"))
            except:
                os.system('cls')
                mistakeCount()
                print(f"\nThat's Not an Integer...\n{reply}")
                printBoard(board)
            else:
                if inp >= 1 and inp <= 9 and board[inp-1] == "-":
                    board[inp-1] = p1Token
                    os.system('cls')
                    break
                elif inp < 1:
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat's Too Small...\n{reply}")
                    printBoard(board)
                elif inp > 9:
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat's Too Big...\n{reply}")
                    printBoard(board)
                elif board[inp-1] != "-":
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat Spot's Already Taken...\n{reply}")
                    printBoard(board)

    def player2Input(board):
        while True:
            try:
                inp = int(input(f"{p2Name}, Enter an Integer 1-9:\n"))
            except:
                os.system('cls')
                mistakeCount()
                print(f"\nThat's Not an Integer...\n{reply}")
                printBoard(board)
            else:
                if inp >= 1 and inp <= 9 and board[inp-1] == "-":
                    board[inp-1] = p2Token
                    os.system('cls')
                    break
                elif inp < 1:
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat's Too Small...\n{reply}")
                    printBoard(board)
                elif inp > 9:
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat's Too Big...\n{reply}")
                    printBoard(board)
                elif board[inp-1] != "-":
                    os.system('cls')
                    mistakeCount()
                    print(f"\nThat Spot's Already Taken...\n{reply}")
                    printBoard(board)

    #---------------------------------------------Play Again?--------------------------------------------------------------------
    def playAgain():
        replay = input(f"Would you like to play again? Yes / No\n")
        while True:
            if "y" in replay or "Y" in replay:
                os.system('cls')
                mainGame()
            elif "n" in replay or "N" in replay:
                os.system('cls')
                sys.exit()
            else:
                print(f"/nCome on now {p1Name}, it's a Yes or No question...\n{reply}\n")


    #---------------------------------------------Check Win/Tie Status-----------------------------------------------------------
    def checkRow(board):
        global winner
        if board[0] == board[1] == board[2] and board[0] != "-":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != "-":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != "-":
            winner = board[6]
            return True
        
    def checkColumn(board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != "-":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
            winner = board[2]
            return True

    def checkDiag(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[2] != "-":
            winner = board[2]
            return True

    def checkWin(board):
        if checkDiag(board) or checkRow(board) or checkColumn(board):
            global winner
            printBoard(board)
            print(f"\nThe Winner is {winner}'s!!!")
            if players == 1:
                if winner == p1Token:
                    print(f"Brains Beat the Bolts! Congratulations, {p1Name}!!!\n")
                    playAgain()
                elif winner == cToken:
                    print(f"The Computer Wins!!! Skynet lives to terminate another day.\n")
                    playAgain()
            elif players == 2:
                if winner == p1Token:
                    print(f"Congratulations, {p1Name}!!! You've bested {p2Name}!")
                    playAgain()
                elif winner == p2Token:
                    print(f"Congratulations, {p2Name}!!! You've bested {p1Name}!")
                    playAgain()

    def checkTie(board):
        if "-" not in board:
            printBoard(board)
            print(f"\nOH NO! It's a Tie...\n")
            playAgain()

    #---------------------------------------------Computer Player Move--------------------------------------------------------
    def computerEasy(board):
        print("The Computer is Thinking...")
        time.sleep(2)
        while True:
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = cToken
                os.system('cls')
                break


    def computerHard(board):
        global winner
        print("The Computer is Thinking... Really Hard!")
        #the enumerate function returns 1st the index of the list item and 2nd the value of the list item
        #this happens in a key:value pair where the index number is the key and the value is the value
        possibleMoves = [index for index, value in enumerate(board) if value == "-"]
        time.sleep(2)
        position = "No Winner"
    #so this is next bit is sticky... It pretty much brute forces the next round of play using both X's and O's
    #if any singular placement is going to win this block will place the computer token in that spot (starting with its own win)
    #this occurs on a first-come first-serve basis, but the computer starts with its own tokens.
        found = False
        for token in [cToken, p1Token]:
            if found:
                break
            for i in possibleMoves:
                boardCopy = board.copy()
                boardCopy[i] = token
                if checkRow(boardCopy) or checkColumn(boardCopy) or checkDiag(boardCopy):
                    position = i
                    board[position] = cToken
                    winner = None
                    found = True
                    os.system('cls')
                    break

        if position == "No Winner":
                ideal = [4, 0, 2, 6, 8]
                for i in ideal:
                    if board[i] == "-":
                        board[i] = cToken
                        os.system('cls')
                        break

        
    def computerMedium(board):
        global winner
        print("The Computer is Thinking... Really Hard!")
        possibleMoves = [index for index, value in enumerate(board) if value == "-"]
        time.sleep(2)
        position = "No Winner"
        found = False
        for token in [cToken, p1Token]:
            if found:
                break
            for i in possibleMoves:
                boardCopy = board.copy()
                boardCopy[i] = token
                if checkRow(boardCopy) or checkColumn(boardCopy) or checkDiag(boardCopy):
                    position = i
                    board[position] = cToken
                    winner = None
                    found = True
                    os.system('cls')
                    break

        if position == "No Winner":
            while True:
                position = random.randint(0, 8)
                if board[position] == "-":
                    board[position] = cToken
                    os.system('cls')
                    break

    #---------------------------------------------Game Run Loop-----------------------------------------------------------
    #This while-loop literally says repeat these functions "while gameRunning = True", which it will do until we specifically
    #switch the gameRunning variable to false. This will only pause to wait for player input during input() functions
    playerNo()
    chooseToken()
    if players == 1:
        setDifficutly()

    while True:
        printBoard(board)
        player1Input(board)
        printBoard(board)
        checkWin(board)
        checkTie(board)
        if players == 2:
            player2Input(board)
        elif players == 1:
            if compDifficulty == "easy":
                computerEasy(board)
            elif compDifficulty == "medium":
                computerMedium(board)
            elif compDifficulty == "hard":
                computerHard(board)
        checkWin(board)
        checkTie(board)
mainGame()