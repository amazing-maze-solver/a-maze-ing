import pytest
from pathlib import Path
import json
from scripts.location_functions import import_data, create_menu_objects
from scripts.location_classes import is_valid_filename

##################################################################################
# location_functions.py


# @pytest.mark.skip()
def test_is_valid_filename(create_path):
    actual = is_valid_filename(create_path.name.replace(".json", ""))
    assert actual is True


# @pytest.mark.skip()
def test_is_valid_filename_fail(create_path):
    actual = is_valid_filename(create_path.name.replace(".json", "?"))
    assert actual is False


# @pytest.mark.skip()
def test_import_data(create_path):
    actual = import_data()
    expected = "intro"
    assert actual.location == "intro"


# @pytest.mark.skip()
def test_create_menu_objects(create_path):
    with create_path.open("r") as file:
        data = json.load(file)
        intro_location = create_menu_objects(data)
    assert intro_location.location == "intro"
    main_location = intro_location.locations.get("main", False)
    assert main_location.location == "main"
    quitting_location = main_location.locations.get("quitting", False)
    assert quitting_location.location == "quitting"

###################################################################################
# location_classes.py










######################################################################################
# fixtures

@pytest.fixture
def create_path():
    path = Path.cwd().joinpath("resources", "text", "location_objects.json")
    return path
