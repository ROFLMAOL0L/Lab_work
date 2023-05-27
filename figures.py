# All figures have a starting point, everything is either a point or has a point in its structure.
class Point:
    def __init__(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y
        self.type = 'Point'


# A Line is two connected points: first one that is a Point() class, and the second one - ending point.
class Line(Point):
    def __init__(self, pos_x1, pos_y1, pos_x2, pos_y2):
        Point.__init__(self, pos_x1, pos_y1)
        self.x_end, self.y_end = pos_x2, pos_y2
        self.type = 'Line'
        # (y - y1) / (y2 - y1) = (x - x1) / (x2 - x1)
        # k = (y2 - y1) / (x2 - x1)
        # b = (x1 * (y1 - y2) ) / (x2 - x1) + y1
        self.k = (pos_y2 - pos_y1) / (pos_x2 - pos_x1)
        self.b = (pos_x1 * (pos_y1 - pos_y2)) / (pos_x2 - pos_x1) + pos_y1
        # Values for an infinite line
        self.x = -500
        self.y = self.k * self.x + self.b
        self.x_end = 500   # This is screen size based on my guess
        self.y_end = self.k * self.x_end + self.b

    def compare(self, c_x, c_y):
        # If a dot is "higher" than the line - it`s True, "lower" - False
        if c_y > self.k * c_x + self.b:
            return True
        else:
            return False


# A Rectangle is a combination of all possible points made out of coordinates of two different points:
# the first one if Point() class and the second one is the opposite rectangle's point.
class Rectangle(Point):
    def __init__(self, pos_x1, pos_y1, pos_x2, pos_y2):
        Point.__init__(self, pos_x1, pos_y1)
        self.x_opposite, self.y_opposite = pos_x2, pos_y2

        # This way of storing vertices allows us to go through them
        # in a clockwise direction if (x2 > x1 and y2 > y1) or (x2 < x1 and y2 < y1)
        # in a counter-clockwise direction if (x2 > x1 and y2 < y1) or (x2 < x1 and y2 > y1)
        self.vertices = [
            (self.x, self.y),
            (self.x, self.y_opposite),
            (self.x_opposite, self.y_opposite),
            (self.x_opposite, self.y)
        ]
        self.type = 'Rectangle'

    def compare(self, c_x, c_y):
        if self.x < c_x < self.x_opposite:
            if self.y < c_y < self.y_opposite:
                return True
        return False


# A Circle is a Point with a radius.
class Circle(Point):
    def __init__(self, pos_x, pos_y, radius):
        Point.__init__(self, pos_x, pos_y)
        self.radius = radius
        self.type = 'Circle'

    def compare(self, c_x, c_y):
        if (self.x + c_x) ** 2 + (self.y + c_y) ** 2 < self.radius ** 2:
            return True
        else:
            return False
