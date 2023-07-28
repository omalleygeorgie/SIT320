from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def begin_game(self):
        pass

    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def check_win(self):
        pass

class AlgorithmInterface(ABC):
    @abstractmethod
    def calculate_move(self):
        pass

class TicTacToe(GameInterface):
    def begin_game(self):
        pass

    def make_move(self):
        pass

    def check_win(self):
        pass

class Backgammon(GameInterface):
    def begin_game(self):
        pass

    def make_move(self):
        pass

    def check_win(self):
        pass

class Chess(GameInterface):
    def begin_game(self):
        pass

    def make_move(self):
        pass

    def check_win(self):
        pass

class Minimax(AlgorithmInterface):
    def calculate_move(self):
        pass

class ReinforcementLearning(AlgorithmInterface):
    def calculate_move(self):
        pass

class GameFactory:
    @staticmethod
    def create_game(game):
        if game == "TicTacToe":
            return TicTacToe()
        elif game == "Backgammon":
            return Backgammon()
        elif game == "Chess":
            return Chess()

class AlgorithmFactory:
    @staticmethod
    def create_algorithm(algorithm):
        if algorithm == "Minimax":
            return Minimax()
        elif algorithm == "ReinforcementLearning":
            return ReinforcementLearning()
