from dataclasses import dataclass
from typing import NamedTuple, Protocol


def tag(name: str, value: str | None = None, **attr):
    """
    Input name of xml element, value to be contained in xml element, and any xml attributes.
    :param name: str
    :param value: str
    :param attribute: dict
    :return: xml as str
    """
    attribute = (
        ""
        if not attr else
        " " + " ".join(f"{name.replace('-','_')}='{value}'" for name, value in attr.items()) )
    if value is not None:
        return f"<{name} {attribute}>{value}</{name}>"
    else:
        return f"<{name} {attribute}></{name}>"


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
        Convert data into svg string.
        """
        return tag("line", x1=self.start.x, y1=self.start.y, x2=self.end.x, y2=self.end.y, **attribute)


class Polyline(tuple[Point,...]):
    """
    Class of connected lines that will not connect to make a complete shape.
    """
    def draw(self, **attributes):
        """
        Convert data into svg string.
        """
        points = " ".join(point.draw() for point in self)
        return tag("polyline", points=points, **attributes)


class Polygon(tuple[Point,...]):
    """

    """







