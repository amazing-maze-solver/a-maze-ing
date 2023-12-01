import array
import struct

from dataclasses import dataclass
from typing import BinaryIO

# TODO: change to "AMAZEING"
MAGIC_NUMBER: bytes = b"MAZE"


@dataclass(frozen=True)
class FileHeader:
    """
    Dataclass to create binary file header for maze.
    """
    format_version: int
    width: int
    height: int

    def write(self, file: BinaryIO) -> None:
        """
        Input file to write header to binary maze file.
        """
        file.write(MAGIC_NUMBER)
        file.write(struct.pack("B"), self.format_version)
        file.write(struct.pack("<2I", self.width, self.height))


@dataclass(frozen=True)
class FileBody:
    """
    Dataclass to create binary file body for maze.
    """
    square_values: array.array

    def write(self, file: BinaryIO) -> None:
        """
        Input file to write body of binary maze file.
        """
        file.write(self.square_values.tobytes())
