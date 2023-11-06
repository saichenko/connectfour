class MoveIsNotValidError(Exception):
    """Move can not be fit in board size."""


class PlaceIsOccupiedError(Exception):
    """Place is already occupied."""


class PlayersAmountExceededError(Exception):
    """Players amount exceeded."""


class PlayerAlreadyExistsError(Exception):
    """Player already exists."""


class NoPlacesLeftError(Exception):
    """No places left."""
