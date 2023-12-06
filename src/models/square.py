from dataclasses import dataclass
from src.models.border import Border
from src.models.role import Role


@dataclass(frozen=True)
class Square:
    """
    dataclass square that holds all square attributes
    """
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE

    def __eq__(self, other):
        if isinstance(other, Square):
            return all([other.index == self.index,
                    other.row == self.row,
                    other.column == self.column,
                    other.border == self.border,
                    other.role == self.role])

        return False




# if __name__ == "__main__":
#     square_test = Square(1, 1, 3, Border.TOP, Role.NONE)
#     square_test2 = Square(1, 1, 3, Border.TOP, Role.NONE)
#     print(square_test2 == square_test)