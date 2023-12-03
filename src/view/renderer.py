import tempfile
import textwrap
import webbrowser
from dataclasses import dataclass

from src.models.maze import Maze
from src.models.role import Role
from src.models.solution import Solution
from src.models.square import Square
from src.view.decomposer import decompose
from src.view.primitives import Point, Polyline, Rect, Text, tag

ROLE_EMOJI = {
    Role.ENTRANCE: "\N{pedestrian}",
    Role.EXIT: "\N{chequered flag}",
    Role.ENEMY: "\N{ghost}",
    Role.REWARD: "\N{white medium star}",
}

@dataclass(frozen=True)
class SVG:
    """"""

    xml_content: str

    @property
    def html_content(self) -> str:
        """"""
        return textwrap.dedent(
            f"""\
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <title>SVG Preview</title>
                </head>
                <body>
                {self.xml_content}
                </body>
                </html>""")

    def preview(self) -> None:
        """"""
        pass


@dataclass(frozen=True)
class SVGRenderer:
    """"""
    square_size: int = 100
    line_width: int = 5

    @property
    def offset(self) -> int:
        """"""
        return self.line_width // 2


    def render(self, maze: Maze, solution: Solution | None = None) -> SVG:
        """"""
        margin = (self.offset + self.line_width)
        width = 2 * margin + maze.width * self.square_size
        height = 2 * margin + maze.height * self.square_size

        return SVG(
            tag("svg",
                self._get_body(maze, solution),
                xmlns="http://www.w3.org/2000/svg",
                stroke_linejoin="round",
                width=width,
                height=height,
                viewBox=f"0 0 {width} {height}",))

    def _get_body(self, maze: Maze, solution: Solution | None) -> str:
        """"""
        return "".join([
            background(),
            *map(self._draw_square, maze)
        ])

    def _draw_square(self, square: Square) -> str:
        """"""
        top_left = self._transform(square)
        collective_xml = []
        if square.role is Role.EXTERIOR:
            exterior_xml = ... #TODO
            collective_xml.append(exterior_xml)
        elif square.role is Role.WALL:
            wall_xml = ... #TODO
            collective_xml.append(wall_xml)
        elif emoji := ROLE_EMOJI.get(square.role):
            emoji_xml = ... #TODO
            collective_xml.append(emoji_xml)
        border_xml = self._draw_border(square, top_left)
        collective_xml.append(border_xml)
        return "".join(collective_xml)

    def _transform(self, square: Square, extra_offset: int=0) -> Point:
        """
        """
        x = square.row * self.square_size
        y = square.column * self.square_size
        top_left_point = Point(x, y).translate(self.offset+extra_offset, self.offset+extra_offset)
        return top_left_point

    def _draw_border(self, square: Square, point: Point) -> str:
        """"""
        return decompose(square.border, point, self.square_size).draw(stroke_width=self.line_width, stroke="black", fill="none")




def background():
    """"""
    return Rect().draw(width="100%", height="100%", fill="white")
