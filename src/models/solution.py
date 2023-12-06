from dataclasses import dataclass
from typing import Iterator

from src.models.role import Role
from src.models.square import Square


@dataclass(frozen=True)
class Solution:
    """
    Dataclass maze solution that holds a tuple of squares.
    """
    squares: tuple[Square, ...]

    def __post_init__(self):
        # validate_solution_corridor(self)
        assert self.squares[0].role is Role.ENTRANCE, "Solution must start with entrance."
        assert self.squares[-1].role is Role.EXIT, "Solution must end with exit."

    def __iter__(self) -> Iterator:
        """
        Returns iterable of solution.
        """
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        """
        Input index return square from maze.
        """
        return self.squares[index]

    def __len__(self) -> int:
        """
        Will return length of maze solution.
        """
        return len(self.squares)

    def __eq__(self, other):
        if isinstance(other, Square):
            return (other.index == self.index
                    and other.row == self.row
                    and other.column == self.column
                    and other.border == self.border
                    and other.role == self.role)
        return False


def validate_solution_corridor(solution) -> None:
    p1, p2 = 0, 1
    solution_length = len(solution)
    while p2 < solution_length:
        square1 = solution[p1]
        square2 = solution[p2]
        if ((square1.row == square2.row and abs(square1.column-square2.column) == 1) or
                (square1.column == square2.column and abs(square1.row-square2.row) == 1)):
            p1 += 1
            p2 += 1
            continue
        else:
            assert False, "Solution must have a corridor from start to exit square."


# if __name__ == "__main__":
#     from src.models.border import Border
#     from src.models.maze import Maze
#     from src.models.role import Role
#     maze = Maze(
#          squares=(
#              Square(0, 0, 0, Border.TOP | Border.LEFT),
#              Square(1, 0, 1, Border.TOP | Border.RIGHT),
#              Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
#              Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
#              Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
#              Square(5, 1, 1, Border.LEFT | Border.RIGHT),
#              Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
#              Square(7, 1, 3, Border.RIGHT),
#              Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
#              Square(9, 2, 1, Border.BOTTOM),
#              Square(10, 2, 2, Border.TOP | Border.BOTTOM),
#              Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
#          )
#      )
#
#     solution = Solution(squares=tuple(maze[i] for i in (8, 9, 10, 11, 7, 6, 2)))
