from sudoku.grid import Grid
from sudoku.cell import Cell


class TestGrid:
    def test_update_cell_when_cell_is_not_set(self):
        value = 5
        x_coordinate = 5
        y_coordinate = 5
        grid = Grid()
        cell = Cell(value)
        grid.add_cell(x_coordinate, y_coordinate, cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == value

    def test_update_cell_when_x_coordinate_is_greater_than_eight(self):
        value = 5
        x_coordinate = 9
        y_coordinate = 5
        grid = Grid()
        cell = Cell(value)
        grid.add_cell(x_coordinate, y_coordinate, cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == 0

    def test_update_cell_when_x_coordinate_is_less_than_zero(self):
        value = 5
        x_coordinate = -1
        y_coordinate = 5
        grid = Grid()
        cell = Cell(value)
        grid.add_cell(x_coordinate, y_coordinate, cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == 0

    def test_update_cell_when_y_coordinate_is_greater_than_eight(self):
        value = 5
        x_coordinate = 5
        y_coordinate = 9
        grid = Grid()
        cell = Cell(value)
        grid.add_cell(x_coordinate, y_coordinate, cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == 0

    def test_update_cell_when_y_coordinate_is_less_than_zero(self):
        value = 5
        x_coordinate = 5
        y_coordinate = -1
        grid = Grid()
        cell = Cell(value)
        grid.add_cell(x_coordinate, y_coordinate, cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == 0

    def test_update_cell_when_existing_cell_is_not_modifiable(self):
        value = 5
        x_coordinate = 0
        y_coordinate = 0
        grid = Grid()
        cell = Cell(value, False)
        grid.add_cell(x_coordinate, y_coordinate, cell)
        new_cell = Cell(6)
        grid.add_cell(x_coordinate, y_coordinate, new_cell)

        cell = grid.get_cell(x_coordinate, y_coordinate)

        assert cell.get_value() == value
