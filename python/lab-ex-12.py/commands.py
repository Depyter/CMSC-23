from board import Board
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class DashUpCommand(Command):
    def __init__(self, board:Board):
        self.__Board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__Board.canMoveUp():
            self.__Board.moveUp()

    def undo(self):
        self.__Board.teleportCharacter(self.__backupLocation)

class DashLeftCommand(Command):
    def __init__(self, board:Board):
        self.__Board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__Board.canMoveLeft():
            self.__Board.moveLeft()

    def undo(self):
        self.__Board.teleportCharacter(self.__backupLocation)


class DashRightCommand(Command):
    def __init__(self, board:Board):
        self.__Board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__Board.canMoveRight():
            self.__Board.moveRight()

    def undo(self):
        self.__Board.teleportCharacter(self.__backupLocation)

class DashDownCommand(Command):
    def __init__(self, board:Board):
        self.__Board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__Board.canMoveDown():
            self.__Board.moveDown()

    def undo(self):
        self.__Board.teleportCharacter(self.__backupLocation)

