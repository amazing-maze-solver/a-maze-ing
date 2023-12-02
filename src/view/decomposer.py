from src.models.border import Border
from src.view.primitives import (
    NullPrimitive,
    Primitive,
    Point,
    Line,
    Polyline,
    Polygon,
    DisjointedLines
)


def decompose(border: Border, top_left: Point, square_size: int) -> Primitive:
    """
    Will return instance of square shape based on square border
    """
    top_right = top_left.translate(x=square_size)
    bottom_right = top_left.translate(x=square_size, y=square_size)
    bottom_left = top_left.translate(y=square_size)

    top = Line(top_left, top_right)
    right = Line(top_right, bottom_right)
    bottom = Line(bottom_left, bottom_right)
    left = Line(bottom_left, top_left)

    if border is Border.TOP | Border.RIGHT | Border.BOTTOM | Border.LEFT:
        return Polygon([top_left, top_right, bottom_right, bottom_left])