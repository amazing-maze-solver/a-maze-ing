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
