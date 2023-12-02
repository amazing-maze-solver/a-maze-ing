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



def load_binary_maze_file(path: pathlib.Path) -> Iterator[Square]:
    """
    Load maze data and return iterable of square elements.
    :param path: pathlib.Path
    :return: Iterator[Square]
    """
    with path.open("rb") as file:
        header = FileHeader.read(file)
        if header.format_version != FORMAT_VERSION:
            raise ValueError("Unsupported file format version.")
        body = FileBody.read(header, file)
        return deserializer(header, body)


def deserializer(header: FileHeader, body: FileBody) -> Iterator[Square]:
    """
    Input FileHeader instance and FileBody instance.
    Output is iterator generator.
    :param header:
    :param body:
    :return:
    """
    for index, square_value in enumerate(body.square_values):
        row, column = divmod(index, header.width)
        border, role = decompress(square_value)
        yield Square(index, row, column, border, role)


def decompress(square_value):
    """
    Input integer and extract binary values.
    :param square_value:
    :return:
    """
    border = Border(square_value & 15) # b'00001111'
    role = Role(square_value >> 4)
    return border, role


# if __name__ == "__main__":
    from src.models.maze import Maze
    # from pathlib import Path
    # path = Path.cwd().parent.parent.joinpath("resources/mazes/miniature.maze")
    # maze = Maze(
    #     squares=(
    #         Square(0, 0, 0, Border.TOP | Border.LEFT),
    #         Square(1, 0, 1, Border.TOP | Border.RIGHT),
    #         Square(2, 0, 2, Border.LEFT | Border.RIGHT, role=Role.EXIT),
    #         Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
    #         Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
    #         Square(5, 1, 1, Border.LEFT | Border.RIGHT),
    #         Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
    #         Square(7, 1, 3, Border.RIGHT),
    #         Square(8, 2, 0, Border.TOP | Border.LEFT, role=Role.ENTRANCE),
    #         Square(9, 2, 1, Border.BOTTOM),
    #         Square(10, 2, 2, Border.TOP | Border.BOTTOM),
    #         Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
    #     )
    # )

    # for square in load_binary_maze_file(path):
    #     print(square)
    # print(Maze(tuple(load_binary_maze_file(path))))
    # path.unlink()