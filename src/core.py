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
    PLAYERS: list[Player]
    IS_GRAVITY_ENABLED: bool

    @abc.abstractmethod
    def add_player(self, player: Player):
        pass

    @abc.abstractmethod
    def add_move(self, player: Player, n: int, m: int):
        pass

    @abc.abstractmethod
    def check_winner(self) -> Player | None:
        pass
