from sudoku.cell import Cell


class Grid:
    CONS_Dimensions = 9

    __grid = [[Cell()]*CONS_Dimensions]*CONS_Dimensions

    def __init__(self):
        pass

    def add_cell(self, x_coordinate, y_coordinate, cell):
        if self.__validate_cell_update(x_coordinate, y_coordinate):
            self.__grid[x_coordinate][y_coordinate] = cell

    def get_cell(self, x_coordinate, y_coordinate):
        return self.__grid[x_coordinate][y_coordinate]

    def __validate_cell_update(self, x_coordinate, y_coordinate):
        if (  0 <= x_coordinate < 9 and 0 <= y_coordinate < 9):
            existing_cell = self.__grid[x_coordinate][y_coordinate]
            return existing_cell.can_modify()

