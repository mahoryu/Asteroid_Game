class Point():
    """
    A point object containing an x and y coordinate
    """
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x},{self._y})"

    # Getters
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    # Setters
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    # Properties
    y = property(getY, setY)
    x = property(getX, setX)