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



# if __name__ == "__main__":
#     square_test = Square(1, "square", 3, Border.TOP, Role.NONE)
#     print(square_test)