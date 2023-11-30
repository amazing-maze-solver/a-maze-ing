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
        validate_maze_entrance(self)
        validate_maze_exit(self)
        validate_maze_indices(self)
        validate_maze_rows_and_columns(self)

    def __iter__(self) -> Iterator[Square]:
        """
        transform maze into iterable
        """
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        """
        input index return square from maze
        """
        return self.squares[index]


    @cached_property
    def width(self) -> int:
        """
        returns max width of the maze
        """
        return max([square.row for square in self]) + 1

    @cached_property
    def height(self) -> int:
        """
        returns max height of the maze
        """
        return max([square.column for square in self]) + 1


def validate_maze_entrance(maze: Maze) -> None:
    """
    raises exception if maze doesn't have exactly one entrance
    """
    count = 0
    for square in maze:
        if square.role is Role.ENTRANCE:
            count += 1
    assert count == 1, "Maze must have exactly one entrance"


def validate_maze_exit(maze: Maze) -> None:
    """
    raises exception if maze doesn't have exactly one exit
    """
    count = 0
    for square in maze:
        if square.role is Role.EXIT:
            count += 1
    assert count == 1, "Maze must have exactly one exit"


def validate_maze_indices(maze: Maze) -> None:
    """
    raises exception if maze squares don't have valid indices
    """
    actual_maze_indices = [square.index for square in maze]
    expected_maze_indices = [i for i in range(len(maze.squares))]
    assert actual_maze_indices == expected_maze_indices, "One or more maze square index value is invalid"


def validate_maze_rows_and_columns(maze: Maze) -> None:
    """
    raises exception if maze squares don't have valid row and column attributes
    """
    for i in range(0, maze.height):
        for j in range(0, maze.width):
            index = i * maze.width + j
            square = maze[index]
            assert square.row == i, f"maze square at {i, j} contains invalid row value"
            assert square.column == j, f"maze square at {i, j} contains invalid column value"


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
    # print(maze.length)