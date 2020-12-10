class Velocity():
    """
    Velocity class to mesure the rate of speed at which
    an object is moving.
    """
    def __init__(self, dX, dY):
        self.dX = dX
        self.dY = dY

    def getDx(self):
        return self.dX

    def getDy(self):
        return self.dY

    def setDx(self, dX):
        self.dX = dX

    def setDy(self, dY):
        self.dY = dY
