import abc

import attrs


@attrs.define(repr=False)
class Player:
    name: str = attrs.field(eq=True, repr=True)

    def __repr__(self):
        return self.name


@attrs.define(repr=False)
class Move:
    player: Player

    def __repr__(self) -> str:
        return str(self.player)


class BoardAbstract(abc.ABC):

    WIDTH: int
    HEIGHT: int
    PLAYERS_AMOUNT: int

    @abc.abstractmethod
    def add_player(self, player: Player):
        pass

    @property
    @abc.abstractmethod
    def board(self) -> list[list[Move | None]]:
        pass

    @property
    @abc.abstractmethod
    def players(self) -> tuple[Player]:
        pass

    @abc.abstractmethod
    def add_move(self, player: Player, n: int, m: int):
        pass

    @abc.abstractmethod
    def check_winner(self) -> Player | None:
        pass
