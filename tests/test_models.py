import pytest
from src.models.role import Role


# @pytest.mark.skip("TODO")
def test_role_exists():
    assert Role


# @pytest.mark.skip("TODO")
def test_role_values():
    variable_list = ["NONE", "ENTRANCE", "EXIT", "WALL", "EXTERIOR"]
    for index, name in enumerate(variable_list):
        assert Role[name] == index