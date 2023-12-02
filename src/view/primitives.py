from dataclasses import dataclass
from typing import NamedTuple, Protocol


def tag(name: str, value: str|None = None, **attribute):
    pass


class NullPrimitive:
    """
    Null class that must contain draw method.
    """
    def draw(self, **attributes) -> str:
        """
        Convert data into svg string.
        """
        return ""


class Primitive(Protocol):
    """
    Class for draw hints that must contain draw method.
    """
    def draw(self, **attributes) -> str:
        """
        Convert data into svg string.
        """
        ... # TODO: change to pass


class Point(NamedTuple):
    """
    Class point to contribute to maze render.
    """
    x: int
    y: int

    def draw(self, **attribute):
        """
        Convert data into svg string.
        """
        return f"{self.x}, {self.y}"

    def translate(self, offset_x: int=0, offset_y: int=0):
        """
        Translate x and y coordinate for point.
        """
        return Point(self.x + offset_x, self.y + offset_y)

class Line(NamedTuple):
    """
    Input self and dictionary of attributes to return xml element of line.
    """
    start: Point
    end: Point

    def draw(self, **attribute):
        """
        Translate x and y coordinate for point.
        """
        return tag("line", x1 = self.start.x, y1 = self.start.y, x2 = self.end.x, y2 = self.end.y, **attribute)







