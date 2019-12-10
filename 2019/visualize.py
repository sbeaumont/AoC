"""
Utility library to easily create visualizations for code challenges (Advent Of Code!!!)

Serge Beaumont, december 2019
"""

from PIL import Image, ImageDraw
from collections import namedtuple


Point = namedtuple('Point', 'x y')
Color = namedtuple('Color', 'R G B')


BACKGROUND_COLOR = Color(R=0, G=0, B=0)
BLOCK = '\u2588'

COLORS = (
    Color(R=255, G=255, B=0),
    Color(R=255, G=0, B=255),
    Color(R=0, G=255, B=255),
    Color(R=255, G=0, B=0),
    Color(R=0, G=255, B=0),
    Color(R=0, G=0, B=255),
    Color(R=255, G=255, B=255)
)


class Visualizer(object):
    def __init__(self, boundaries, scale=1, flip_vertical=True):
        """boundaries allows you to set x and y boundaries that correspond to the puzzle values.
        This class will then calculate how this maps onto the image.

        Note that scale only scales coordinates, not line widths. Set those separately."""
        self.scale = scale
        self.flip_vertical = flip_vertical
        x1, y1, x2, y2 = boundaries
        self.b_min = self._scale_point(Point(x1, y1))
        self.b_max = self._scale_point(Point(x2, y2))
        self.im = Image.new('RGB', \
                            (abs(self.b_max.x - self.b_min.x), \
                             abs(self.b_max.y - self.b_min.y)), \
                            BACKGROUND_COLOR)
        self.draw = ImageDraw.Draw(self.im)

    def _scale_point(self, p: Point) -> Point:
        return Point(p.x * self.scale, p.y * self.scale)

    def _to_image_coords(self, point) -> Point:
        p = Point(*point)
        # To create larger images of small coordinate spaces in a puzzle
        p = self._scale_point(p)
        # To deal with x and y values that are negative in the puzzle. Shift to positive image coordinates.
        p = Point(p.x - self.b_min.x, p.y - self.b_min.y)
        # Image origin is top left, needs to be bottom left.
        if self.flip_vertical:
            p = Point(p.x, self.im.height - p.y)
        return p

    def draw_point(self, point, color, size=1):
        p = self._to_image_coords(point)
        self.draw.ellipse((p.x - size, p.y - size, p.x + size, p.y + size), fill=color)

    def draw_points(self, points, color, size=1):
        for point in points:
            self.draw_point(point, color, size)

    def draw_line(self, line, color, width=1):
        x1, y1 = self._to_image_coords(line[0])
        x2, y2 = self._to_image_coords(line[1])
        self.draw.line((x1, y1, x2, y2), color, width=width)

    def draw_lines(self, lines, color, width=1):
        for line in lines:
            self.draw_line(line, color, width=width)

    def draw_polyline(self, points, color, width=1):
        for i in range(1, len(points)):
            self.draw_line((points[i-1], points[i]), color, width)

    def show(self):
        self.im.show()


if __name__ == '__main__':
    # At scale 2 this coordinate system will lead to a 420 x 420 pixel image.
    viz = Visualizer((0, 0, 210, 210), scale=2)

    # Draw a single line
    viz.draw_line(((10, 20), (50, 100)), COLORS[0], width=5)

    # Draw a list of four lines
    lines = (((110, 10), (200, 10)), ((200, 10), (200, 100)), ((200, 100), (110, 100)), ((110, 100), (110, 10)))
    viz.draw_lines(lines, COLORS[1], width=5)

    # Draw a polyline based on a list of points
    points = ((10, 110), (100, 110), (100, 200), (10, 200), (10, 110))
    viz.draw_polyline(points, COLORS[2], width=5)

    # Draw separate points
    points2 = ((120, 120), (140, 140), (160, 160), (180, 180))
    viz.draw_points(points2, COLORS[3], size=10)

    viz.show()
