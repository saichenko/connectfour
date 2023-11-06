from core import BoardAbstract, Move, Player
from exceptions import (MoveIsNotValidError, NoPlacesLeftError,
                        PlaceIsOccupiedError, PlayerAlreadyExistsError,
                        PlayersAmountExceededError)
import copy


class Board(BoardAbstract):

    WIDTH = 4
    HEIGHT = 4
    PLAYERS_AMOUNT = 2
    IS_GRAVITY_ENABLED = True
    POINTS_TO_WIN = 4

    def __init__(self):
        self.__players: list[Player] = []
        self.__board: list[list[Move | None]] = [
            [None] * self.WIDTH
            for _ in range(self.HEIGHT)
        ]

    @property
    def board(self) -> list[list[Move | None]]:
        return copy.deepcopy(self.__board)

    @property
    def players(self) -> tuple[Player]:
        return tuple(self.__players)

    def add_player(self, player: Player):
        if len(self.__players) >= self.PLAYERS_AMOUNT:
            raise PlayersAmountExceededError
        if player in self.__players:
            raise PlayerAlreadyExistsError
        self.__players.append(player)

    def __check_vertical_winner(self) -> Player | None:
        board = self.__board
        for col in range(len(board[0])):
            for row in range(len(board) - 3):
                if all(board[row + i][col] and board[row + i][col].player == board[row][col].player for i in range(self.POINTS_TO_WIN)):
                    return board[row][col].player
        return None

    def check_horizontal_winner(self) -> Player | None:
        board = self.__board
        for row in range(len(board)):
            for col in range(len(board[0]) - 3):
                if all(board[row][col + i] and board[row][col + i].player == board[row][col].player for i in range(self.POINTS_TO_WIN)):
                    return board[row][col].player
        return None

    def check_diagonal_winner(self) -> Player | None:
        board = self.__board
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                if all(board[row + i][col + i] and board[row + i][col + i].player == board[row][col].player for i in range(self.POINTS_TO_WIN)):
                    return board[row][col].player

        for row in range(3, len(board)):
            for col in range(len(board[0]) - 3):
                if all(board[row - i][col + i] and board[row - i][col + i].player == board[row][col].player for i in range(self.POINTS_TO_WIN)):
                    return board[row][col].player

        return None

    def __check_places_left(self) -> bool:
        for row in self.__board:
            for cell in row:
                if cell is None:
                    return True
        return False

    def check_winner(self) -> Player | None:
        if (player := self.check_horizontal_winner()) is not None:
            return player
        if (player := self.__check_vertical_winner()) is not None:
            return player
        if (player := self.check_diagonal_winner()) is not None:
            return player

        if not self.__check_places_left():
            raise NoPlacesLeftError

    def add_move(self, player: Player, n: int, m: int):
        if (n < 0 or n >= self.HEIGHT) or (m < 0 or m >= self.WIDTH):
            raise MoveIsNotValidError

        if not self.IS_GRAVITY_ENABLED:
            if self.__board[n][m] is not None:
                raise PlaceIsOccupiedError
            self.__board[n][m] = Move(player=player)
            return

        if not any(map(lambda x: x is None, self.__board[n])):
            raise PlaceIsOccupiedError

        # for n_dem in range(self.HEIGHT):
        for m_dem in range(self.WIDTH):
            if self.__board[n][m_dem] is None:
                self.__board[n][m_dem] = Move(player=player)
                return
