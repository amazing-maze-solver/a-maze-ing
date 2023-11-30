from enum import IntEnum


class Role(IntEnum):
    """
    class IntEnum for square role
    """
    NONE = 0
    ENTRANCE = 1
    EXIT = 2
    WALL = 3
    EXTERIOR = 4

