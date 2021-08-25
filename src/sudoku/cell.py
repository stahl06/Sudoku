class Cell:
    __value = 0
    __can_modify = True

    def __init__(self, value=0, can_modify=True):
        self.__can_modify = can_modify
        self.__value = value

    def set_value(self, value):
        if self.__can_modify and  0 <= value <= 9:
            self.__value = value

    def get_value(self):
        return self.__value

    def can_modify(self):
        return self.__can_modify