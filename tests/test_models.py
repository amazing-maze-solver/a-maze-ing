import pytest
from src.models.border import Border
from src.models.role import Role


################################################################################################################
# Role


# @pytest.mark.skip("TODO")
def test_role_exists():
    assert Role


# @pytest.mark.skip("TODO")
def test_role_values():
    variable_list = ["NONE", "ENTRANCE", "EXIT", "WALL", "EXTERIOR"]
    for index, name in enumerate(variable_list):
        assert Role[name] == index


###############################################################################################################
# Border

#@pytest.mark.skip("TODO")
def test_border_exists():
    assert Border


#@pytest.mark.skip("TODO")
def test_border_values():
    variable_list = ["EMPTY", "TOP", "RIGHT", "BOTTOM", "LEFT"]
    index_list = [0, 1, 8, 2, 4]
    for index, name in enumerate(variable_list):
        assert Border[name] == index_list[index]


# @pytest.mark.skip("TODO")
def test_border_corner():
    top_right = Border(Border.TOP | Border.RIGHT).corner
    right_bottom = Border(Border.RIGHT | Border.BOTTOM).corner
    bottom_left = Border(Border.BOTTOM | Border.LEFT).corner
    left_top = Border(Border.LEFT | Border.TOP).corner
    assert top_right and right_bottom and bottom_left and left_top


# @pytest.mark.skip("TODO")
def test_dead_end():
    assert all([Border(Border.TOP | Border.RIGHT | Border.BOTTOM).dead_end,
                Border(Border.RIGHT | Border.BOTTOM | Border.LEFT).dead_end,
                Border(Border.BOTTOM | Border.LEFT | Border.TOP).dead_end,
                Border(Border.LEFT | Border.TOP | Border.RIGHT).dead_end])


# @pytest.mark.skip("TODO")
def test_intersection():
    assert all([Border(Border.EMPTY).intersection, Border(Border.TOP).intersection, Border(Border.RIGHT).intersection,
                Border(Border.BOTTOM).intersection, Border(Border.LEFT).intersection])



# @pytest.mark.skip("TODO")
# @pytest.mark.skip("TODO")
