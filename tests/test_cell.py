from sudoku.cell import Cell


class TestCell:

    def test_set_value_to_less_than_zero(self):
        cell = Cell()
        previous_value = cell.get_value()
        cell.set_value(-1)
        assert cell.get_value() == previous_value

    def test_set_value_to_zero(self):
        cell = Cell()
        cell.set_value(0)
        assert cell.get_value() == 0

    def test_set_value_to_five(self):
        cell = Cell()
        cell.set_value(5)
        assert cell.get_value() == 5

    def test_set_value_to_nine(self):
        cell = Cell()
        cell.set_value(9)
        assert cell.get_value() == 9

    def test_set_value_to_greater_than_nine(self):
        cell = Cell()
        previous_value = cell.get_value()
        cell.set_value(10)
        assert cell.get_value() == previous_value

    def test_set_value_when_can_modify_is_false(self):
        value = 10
        cell = Cell(value, False)
        cell.set_value(0)
        assert cell.get_value() == value
