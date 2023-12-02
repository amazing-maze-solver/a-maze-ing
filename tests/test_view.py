import pytest
from src.view.primitives import NullPrimitive, Point, Line, Polyline, Polygon, DisjointedLines, Rect, Text


# @pytest.mark.skip()
def test_null_primitive():
    assert "" == NullPrimitive().draw(x=1, y=2)


# @pytest.mark.skip()
def test_point():
    actual = Point(100, 200).translate(100, 200).draw()
    expected = f"{200}, {400}"
    assert actual == expected


# @pytest.mark.skip()
def test_line(create_line):
    actual = create_line.draw(a=1, b=2)
    expected = "<line  x1='1' y1='1' x2='2' y2='1' a='1' b='2' />"
    assert actual == expected


# @pytest.mark.skip()
def test_polyline(create_polyline):
    actual = create_polyline.draw(a=1, b=2)
    expected = "<polyline  points='1, 1 2, 1 2, 2' a='1' b='2' />"
    assert actual == expected


# @pytest.mark.skip()
def test_polygon(create_polygon):
    actual = create_polygon.draw(a=1, b=2)
    expected = "<polygon  points='1, 1 2, 1 2, 2' a='1' b='2' />"
    assert actual == expected


# @pytest.mark.skip()
def test_disjointed_lines(create_disjointed_lines):
    actual = create_disjointed_lines.draw(a=1)
    expected = "<line  x1='1' y1='1' x2='2' y2='1' a='1' /><line  x1='1' y1='2' x2='2' y2='2' a='1' />"
    assert actual == expected


# @pytest.mark.skip()
def test_rect(create_rect):
    actual_zero = create_rect[0].draw(width="100%", height="100%", fill="white")
    expected_zero = "<rect  width='100%' height='100%' fill='white' x='1' y='1' />"
    actual_one = create_rect[1].draw(width="100%", height="100%", fill="white")
    expected_one = "<rect  width='100%' height='100%' fill='white' />"
    assert actual_zero == expected_zero
    assert actual_one == expected_one


# @pytest.mark.skip()
def test_text(create_text):
    actual = create_text.draw(a=1, b=2)
    expected = "<text  x='1' y='1' a='1' b='2'>🚶</text>"
    assert actual == expected


@pytest.fixture
def create_line():
    # line
    return Line(Point(1, 1), Point(2, 1))


@pytest.fixture
def create_polyline():
    return Polyline([Point(1, 1), Point(2, 1), Point(2, 2)])


@pytest.fixture
def create_polygon():
    return Polygon([Point(1, 1), Point(2, 1), Point(2, 2)])


@pytest.fixture
def create_disjointed_lines():
    return DisjointedLines([Line(Point(1, 1), Point(2, 1)), Line(Point(1, 2), Point(2, 2))])


@pytest.fixture
def create_rect():
    return Rect(Point(1, 1)), Rect()


@pytest.fixture()
def create_text():
    return Text("\N{pedestrian}", Point(1, 1))


