class Point():
    """
    A point object containing an x and y coordinate
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x},{self._y})"

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    y = property(get_y, set_y)
    x = property(get_x, set_x)