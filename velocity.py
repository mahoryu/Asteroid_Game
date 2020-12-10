class Velocity():
    """
    Velocity class to mesure the rate of speed at which
    an object is moving.
    """
    def __init__(self, dX, dY):
        self._dX = dX
        self._dY = dY

    def getDx(self):
        return self._dX

    def getDy(self):
        return self._dY

    def setDx(self, dX):
        self._dX = dX

    def setDy(self, dY):
        self._dY = dY

    dX = property(getDx, setDx)
    dY = property(getDy, setDy)