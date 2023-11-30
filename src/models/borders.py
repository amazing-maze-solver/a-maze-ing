from enum import IntFlag, auto


class Border(IntFlag):
    """
    class IntFlag enum for square borders
    """
    EMPTY = 0
    TOP = auto()
    RIGHT = auto()
    BOTTOM = auto()
    LEFT = auto()

    @property
    def corner(self) -> bool:
        """
        will check self if square border is a corner
        """
        return self in (
            self.TOP | self.RIGHT,
            self.RIGHT | self.BOTTOM,
            self.BOTTOM | self.LEFT,
            self.LEFT | self.TOP
        )

