import pytest

from pathlib import Path

from src.models.border import Border
from src.models.maze import Maze
from src.models.role import Role
from src.models.square import Square
from src.persistence.serializer import compress, write_binary_maze_file


# @pytest.mark.skip("TODO")
def test_compress():
    square = Square(0, 0, 0, Border.TOP, Role.ENTRANCE)
    actual = compress(square)
    assert actual == 17


# @pytest.mark.skip()
def test_write_binary_maze_file(create_maze):
    maze = create_maze
    path = Path.cwd().joinpath("resources/mazes/test.maze")
    maze.write_file(path)
    if not path.exists():
        assert False
    else:
        path.unlink()


@pytest.fixture
def create_maze():
    maze = Maze(
        squares=(
            Square(0, 0, 0, Border.TOP | Border.LEFT),
            Square(1, 0, 1, Border.TOP | Border.RIGHT),
            Square(2, 0, 2, Border.LEFT | Border.RIGHT, role=Role.EXIT),
            Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
            Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
            Square(5, 1, 1, Border.LEFT | Border.RIGHT),
            Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
            Square(7, 1, 3, Border.RIGHT),
            Square(8, 2, 0, Border.TOP | Border.LEFT, role=Role.ENTRANCE),
            Square(9, 2, 1, Border.BOTTOM),
            Square(10, 2, 2, Border.TOP | Border.BOTTOM),
            Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
        )
    )
    # print(isinstance(maze, Maze))
    return maze
