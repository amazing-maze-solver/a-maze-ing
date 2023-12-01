import array
import pathlib
from typing import Iterator

from src.models.border import Border
from src.models.role import Role
from src.models.square import Square
from src.persistence.file_format import FileBody, FileHeader


FORMAT_VERSION: int = 1


def write_binary_maze_file(path: pathlib.Path, squares: tuple[Square, ...], width: int, height: int) -> None:
    """
    Input file path object, maze squares, width, and height to binary maze file.
    """
    header = FileHeader(FORMAT_VERSION, width, height)
    body = FileBody(array.array("B", map(compress, squares)))
    with path.open(mode="wb") as file:
        header.write(file)
        body.write(file)



def compress(square: Square) -> int:
    """
    Compress role and border values into an integer.
    """
    return (square.role << 4) | square.border.value