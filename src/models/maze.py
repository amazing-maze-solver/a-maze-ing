from dataclasses import dataclass
from functools import cached_property
from typing import Iterator
from pathlib import Path

from src.models.role import Role
from src.models.square import Square


@dataclass(frozen=True)
class Maze:
    """
    dataclass Maze represents maze as tuple of squares
    """
    squares: tuple[Square]

    def __post_init__(self) -> None:
        """
        raises exception if maze fails validation
        """
        validate_entrance(self)

    def __iter__(self) -> Iterator[Square]:
        """
        transform maze into iterable
        """
        return iter(self.squares)


def validate_entrance(maze: Maze) -> None:
    """
    raises exception if maze doesn't have exactly one entrance
    """
    count = 0
    for square in maze:
        if square.role is Role.ENTRANCE:
            count += 1
    assert count == 1, "Maze must have exactly one entrance"


if __name__ == "__main__":
    from src.models.border import Border
    maze = Maze(
         squares=(
             Square(0, 0, 0, Border.TOP | Border.LEFT),
             Square(1, 0, 1, Border.TOP | Border.RIGHT),
             Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
             Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
             Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
             Square(5, 1, 1, Border.LEFT | Border.RIGHT),
             Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
             Square(7, 1, 3, Border.RIGHT),
             Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
             Square(9, 2, 1, Border.BOTTOM),
             Square(10, 2, 2, Border.TOP | Border.BOTTOM),
             Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
         )
     )