import math
import networkx as nx

from typing import NamedTuple, TypeAlias

from src.models.border import Border
from src.models.maze import Maze
from src.models.maze import Role
from src.models.solution import Solution
from src.models.square import Square


Node: TypeAlias = Square


class Edge(NamedTuple):
    node_one: Node
    node_two: Node

    @property
    def flip(self):
        return Edge(self.node_two, self.node_one)

    @property
    def distance(self) -> float:
        return math.dist((self.node_one.row, self.node_one.column), (self.node_two.row, self.node_two.column))


def solve(maze: Maze) -> Solution | None:
    try:
        return Solution(squares=tuple(nx.shortest_path(make_graph(maze), source=maze.entrance, target=maze.exit, weight="weight")))
    except nx.NetworkXException:
        return None


def make_graph(maze: Maze) -> nx.DiGraph:
    nodes = get_nodes(maze)
    directed_edges = get_directed_edges(maze, nodes)
    edges_with_distance = [(edge.node_one, edge.node_two, {"weight": edge.distance}) for edge in directed_edges]
    graph = nx.DiGraph(edges_with_distance)
    return graph


def get_directed_edges(maze: Maze, nodes: set[Node]) -> set[Edge]:
    edges = get_edges(maze, nodes)
    flip_edges = {edge.flip for edge in edges}
    directed_edges = edges | flip_edges
    return directed_edges


def get_nodes(maze: Maze) -> set[Node]:
    nodes = set()
    for square in maze:
        if square.role in (Role.EXTERIOR, Role.WALL):
            continue
        if square.role is not Role.NONE:
            nodes.add(square)
        # if (
        #         square.border.intersection
        #         or square.border.dead_end
        #         or square.border.corner
        # ):
        nodes.add(square)
    return nodes


def get_edges(maze: Maze, nodes: set[Node]) -> set[Edge]:
    edges: set[Edge] = set()
    for source_node in nodes:
        # traverse right
        node = source_node

        # start traverse one column right of current
        for x in range(node.column + 1, maze.width):
            # if current node has right border, break
            if node.border & Border.RIGHT:
                break
            # reassign right adjacent node to current node
            node = maze.squares[node.row * maze.width + x]
            # if new current node is already in set of nodes
            # create new edge, add to edge set, and break
            if node in nodes:
                edges.add(Edge(source_node, node))
                break
        # traverse down
        node = source_node
        # start traverse one row below current
        for y in range(node.row + 1, maze.height):
            # if current node has bottom border, break
            if node.border & Border.BOTTOM:
                break
            # reassign bottom adjacent border to current
            node = maze.squares[y * maze.width + node.column]
            # if new current node is already in set of nodes
            # create new edge, add to edge set, and break
            if node in nodes:
                edges.add(Edge(source_node, node))
                break
    return edges


if __name__ == "__main__":
    from src.models.border import Border
    maze = Maze(
        squares=(
            Square(0, 0, 0, Border.TOP | Border.LEFT),
            Square(1, 0, 1, Border.TOP | Border.RIGHT),
            Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
            Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
            Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
            Square(5, 1, 1, Border.LEFT | Border.RIGHT),
            Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
            Square(7, 1, 3, Border.RIGHT),
            Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
            Square(9, 2, 1, Border.BOTTOM),
            Square(10, 2, 2, Border.TOP | Border.BOTTOM),
            Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
        )
    )

    # solution_f = Solution(squares=tuple(maze[i] for i in (8, 11, 7, 6, 2)))
    solution_t = Solution(squares=tuple(maze[i] for i in (8, 9, 10, 11, 7, 6, 2)))
    # print(solution_t)
    solution_new = solve(maze)
    print("solution_t", [square.index for square in solution_t])
    print("\nsolution new", [square.index for square in solution_new])