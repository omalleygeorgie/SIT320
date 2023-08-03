import random
from abc import ABC, abstractmethod

class Board(ABC):
    @abstractmethod
    def printBoard(self):
        pass

    @abstractmethod
    def spaceIsFree(self, position):
        pass

    @abstractmethod
    def insertLetter(self, letter, position):
        pass

class ThreeByThreeBoard(Board):
    def __init__(self):
        self.board = {1: ' ', 2: ' ', 3: ' ',
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}

    def printBoard(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-+-+-')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print('-+-+-')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
        print('\n')

    def spaceIsFree(self, position):
        if self.board[position] == ' ':
            return True
        else:
            return False

    def insertLetter(self, letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
            self.printBoard()

            if GameManager.chkDraw(self):
                print('Draw!')
            elif GameManager.chkForWin(self):
                if letter == 'X':
                    print('Bot wins!')
                else:
                    print('You win!')
            return True
        else:
            print('Position taken, please pick a different position.')
            return False

class FiveByFiveBoard(Board):
    pass

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def makeMove(self, board):
        pass

class HumanPlayer(Player):
    def makeMove(self, board):
        while True:
            position = int(input(f'Enter position for {self.symbol}: '))
            if board.insertLetter(self.symbol, position):
                break

class BotPlayer(Player):
    def __init__(self, symbol, depth):
        super().__init__(symbol)
        self.depth = depth

    def makeMove(self, board):
        bestScore = -1000
        bestMove = 0

        if len([v for v in board.board.values() if v != ' ']) == 0:
            bestMove = random.choice(list(board.board.keys()))
        else:
            for key in board.board.keys():
                if board.board[key] == ' ':
                    board.board[key] = self.symbol
                    score = self.minimax(board, self.depth, False)
                    board.board[key] = ' '
                    if score > bestScore:
                        bestScore = score
                        bestMove = key

        board.insertLetter(self.symbol, bestMove)

class Algorithm(ABC):
    @abstractmethod
    def algorithm(self, board):
        pass

class Minimax(Algorithm):
    def algorithm(self, board, depth, isMaximizing):
        if GameManager.chkMarkForWin(board, bot):
            return 1
        elif GameManager.chkMarkForWin(board, player):
            return -1
        elif GameManager.chkDraw(board) or depth == 0:
            return 0

        if isMaximizing:
            bestScore = -1000
            for key in board.board.keys():
                if board.board[key] == ' ':
                    board.board[key] = bot
                    score = self.minimax(board, depth - 1, False)
                    board.board[key] = ' '
                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:
            bestScore = 1000
            for key in board.board.keys():
                if board.board[key] == ' ':
                    board.board[key] = player
                    score = self.minimax(board, depth - 1, True)
                    board.board[key] = ' '
                    if score < bestScore:
                        bestScore = score
            return bestScore

class ReinforcementLearning(Algorithm):
    pass

class GameManager:
    @staticmethod
    def chkDraw(board):
        for key in board.board.keys():
            if board.board[key] == ' ':
                return False
        return True

    @staticmethod
    def chkForWin(board):
        if (board.board[1] == board.board[2] and board.board[1] == board.board[3] and board.board[1] != ' '):
            return True
        elif (board.board[4] == board.board[5] and board.board[4] == board.board[6] and board.board[4] != ' '):
            return True
        elif (board.board[7] == board.board[8] and board.board[7] == board.board[9] and board.board[7] != ' '):
            return True
        elif (board.board[1] == board.board[5] and board.board[1] == board.board[9] and board.board[1] != ' '):
            return True
        elif (board.board[3] == board.board[5] and board.board[3] == board.board[7] and board.board[3] != ' '):
            return True
        elif (board.board[1] == board.board[4] and board.board[1] == board.board[7] and board.board[1] != ' '):
            return True
        elif (board.board[2] == board.board[5] and board.board[2] == board.board[8] and board.board[2] != ' '):
            return True
        elif (board.board[3] == board.board[6] and board.board[3] == board.board[9] and board.board[3] != ' '):
            return True
        else:
            return False

    @staticmethod
    def chkMarkForWin(board, mark):
        if (board.board[1] == board.board[2] and board.board[1] == board.board[3] and board.board[1] == mark):
            return True
        elif (board.board[4] == board.board[5] and board.board[4] == board.board[6] and board.board[4] == mark):
            return True
        elif (board.board[7] == board.board[8] and board.board[7] == board.board[9] and board.board[7] == mark):
            return True
        elif (board.board[1] == board.board[5] and board.board[1] == board.board[9] and board.board[1] == mark):
            return True
        elif (board.board[3] == board.board[5] and board.board[3] == board.board[7] and board.board[3] == mark):
            return True
        elif (board.board[1] == board.board[4] and board.board[1] == board.board[7] and board.board[1] == mark):
            return True
        elif (board.board[2] == board.board[5] and board.board[2] == board.board[8] and board.board[2] == mark):
            return True
        elif (board.board[3] == board.board[6] and board.board[3] == board.board[9] and board.board[3] == mark):
            return True
        else:
            return False

    @staticmethod
    def playGame(human_player, bot_player, board):
        while not GameManager.chkForWin(board) and not GameManager.chkDraw(board):
            bot_player.makeMove(board)
            if GameManager.chkForWin(board) or GameManager.chkDraw(board):
                break
            human_player.makeMove(board)

player = 'O'
bot = 'X'
depth = 4

humanPlayer = HumanPlayer(player)
botPlayer = BotPlayer(bot, depth)

gamemanager = GameManager()

play_again = 'yes'
while play_again == 'yes':
    board = Board()
    gamemanager.playGame(humanPlayer, botPlayer, board)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing. Goodbye!")