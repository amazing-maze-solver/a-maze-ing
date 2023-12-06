import time
from pathlib import Path
import json
import re
import argparse

from src.solve.solver import solve
from src.models.maze import Maze
from src.view.renderer import SVGRenderer
from scripts.location_classes import (
    Location,
    TransitMixin,
    SolveMazeMixin,
    CreateMazeMixin,
    LoadMazeMixin,
    SaveMazeMixin,
    QuittingMixin,
    GoodByeMixin,
    ViewMazeMixin,
    SaveImageMixin,
    SaveSolutionMixin,
    DeleteMixin
)

sleep_in_seconds = 0.2

def sleep(multiple):
    """"""
    time.sleep(sleep_in_seconds*multiple)


def import_data() -> Location:
    """"""
    cwd = Path.cwd()
    path_messages = cwd.joinpath("resources", "text", "location_objects.json")
    with path_messages.open("r") as file:
        data = json.load(file)
        return_object = create_menu_objects(data)
    return return_object


def create_menu_objects(dict_import: dict) -> Location:
    dict_menu = {}
    for key, value in dict_import.items():
        if value.get("mixin") == "TransitMixin":
            location_new = type("TransitLocation", (Location, TransitMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "CreateMazeMixin":
            location_new = type("CreateMazeLocation", (Location, CreateMazeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "SolveMazeMixin":
            location_new = type("SolveMazeLocation", (Location, SolveMazeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "LoadMazeMixin":
            location_new = type("LoadMazeLocation", (Location, LoadMazeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "SaveMazeMixin":
            location_new = type("SaveMazeLocation", (Location, SaveMazeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "ViewMazeMixin":
            location_new = type("ViewMazeLocation", (Location, ViewMazeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "QuittingMixin":
            location_new = type("QuittingLocation", (Location, QuittingMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "GoodByeMixin":
            location_new = type("GoodByeLocation", (Location, GoodByeMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "SaveImageMixin":
            location_new = type("SaveImageLocation", (Location, SaveImageMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "SaveSolutionMixin":
            location_new = type("SaveSolutionLocation", (Location, SaveSolutionMixin), {})
            dict_menu[key] = location_new(**value)
        elif value.get("mixin") == "DeleteMixin":
            location_new = type("DeleteLocation", (Location, DeleteMixin), {})
            dict_menu[key] = location_new(**value)

    for menu in dict_menu.values():
        list_locations = {}
        for name, child in menu.locations.items():
            list_locations[name] = dict_menu.get(name)
        menu.locations = list_locations

    return dict_menu.get("intro")

# TODO: add solve functionality to menu
def solve_maze() -> None:
    maze = Maze.read_file(parse_path())
    solutions = solve(maze)
    if solutions:
        renderer = SVGRenderer()
        for solution in solutions:
            renderer.render(maze, solution).preview()
    else:
        print("No solution found")


def parse_path() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    return parser.parse_args().path


# if __name__=="__main__":

