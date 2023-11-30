from enum import IntEnum, auto


class Role(IntEnum):
    """
    class IntEnum for square role
    """
    NONE = 0
    ENTRANCE = auto()
    EXIT = auto()
    WALL = auto()
    EXTERIOR = auto()

