class Rectangle:
    """
    Represents a rectangle with coordinates (x, y) and dimensions (width, height).
    """

    def __init__(self, x, y, width, height):
        """
        Initializes a new Rectangle instance.

        :param x: The x-coordinate of the top-left corner.
        :param y: The y-coordinate of the top-left corner.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains_point(self, point):
        """
        Checks if the given point is inside the rectangle.

        :param point: A tuple representing the (x, y) coordinates of the point.
        :return: True if the point is inside the rectangle, False otherwise.
        """
        x, y = point
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height


class ExcludedAreas:
    """
    Represents areas that will be excluded (masked) in the image.
    """

    def __init__(self, excluded=None):
        """
        Initializes a new ExcludedAreas instance.

        :param excluded: A list of Rectangle objects representing excluded areas (optional).
        """
        self.excluded = excluded or []

    def contains(self, point):
        """
        Checks if the given point is inside any of the excluded areas.

        :param point: A tuple representing the (x, y) coordinates of the point.
        :return: True if the point is inside any of the excluded areas, False otherwise.
        """
        return any(rectangle.contains_point(point) for rectangle in self.excluded)

    def get_excluded(self):
        """
        Getter for the list of excluded rectangles.

        :return: A list of Rectangle objects representing excluded areas.
        """
        return self.excluded
