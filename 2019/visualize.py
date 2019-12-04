"""
Utility library to easily create visualizations for code challenges (Advent Of Code!!!)

Serge Beaumont, december 2019
"""

from PIL import Image, ImageDraw

BACKGROUND_COLOR = (0, 0, 0)

COLORS = (
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 255)
)


class Visualizer(object):
    def __init__(self, boundaries):
        self.min_x, self.min_y, self.max_x, self.max_y = boundaries
        self.im = Image.new('RGB', \
                            (abs(self.max_x - self.min_x), \
                             abs(self.max_y - self.min_y)), \
                            BACKGROUND_COLOR)
        self.draw = ImageDraw.Draw(self.im)

    def _rotate_left(self, point):
        return point[1], self.max_x - point[0]

    def _to_image_coords(self, point):
        return self._rotate_left((point[0] - self.min_x, point[1] - self.min_y))

    def draw_point(self, point, color, size=1):
        p = self._to_image_coords(point)
        self.draw.ellipse((p[0] - size, p[1] - size, p[0] + size, p[1] + size), fill=color)

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
    viz = Visualizer((0, 0, 210, 210))
    viz.draw_line(((10, 10), (100, 100)), COLORS[0], width=5)
    lines = (((110, 10), (200, 10)), ((200, 10), (200, 100)), ((200, 100), (110, 100)), ((110, 100), (110, 10)))
    viz.draw_lines(lines, COLORS[1], width=5)
    points = ((10, 110), (100, 110), (100, 200), (10, 200), (10, 110))
    viz.draw_polyline(points, COLORS[2], width=5)
    points2 = ((120, 120), (140, 140), (160, 160), (180, 180))
    viz.draw_points(points2, COLORS[3], size=10)
    viz.show()
