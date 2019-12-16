import curses


class CursesVisualizer(object):
    @classmethod
    def boundaries(cls, pts, padding=0):
        """Convenience function to calculate boundaries that will nicely fit all coordinates to be drawn.
        Only useful if all points are known before drawing."""
        min_x = min([p[0] for p in pts])
        max_x = max([p[0] for p in pts])
        min_y = min([p[1] for p in pts])
        max_y = max([p[1] for p in pts])
        return (min_x - padding, min_y - padding), (max_x + padding, max_y + padding)

    def __init__(self, boundaries=((0, 0), (100, 100))):
        self.boundaries = boundaries
        self.b_min = boundaries[0]
        self.b_max = boundaries[1]
        self.stdscr = None

    @property
    def width(self):
        # +1 so we can use b_max,
        # and an extra +1 because curses borks when you put something bottom right.
        # ...an extra column in the pad doesn't matter that much.
        return abs(self.b_max[0] - self.b_min[0]) + 2

    @property
    def height(self):
        # One extra height because of the annoying "exited with code 0" scroll-up,
        # losing the top of what was drawn.
        return abs(self.b_max[1] - self.b_min[1]) + 2

    def _to_pad_xy(self, xy):
        shift_to_origin = (xy[0] - self.b_min[0], xy[1] - self.b_min[1])
        flipped = (shift_to_origin[0], self.height - 1 - shift_to_origin[1])
        return flipped[1], flipped[0]

    def plot(self, point, s):
        p = self._to_pad_xy(point)
        assert (0 <= p[0] <= self.width - 1) and (0 <= p[1] <= self.height - 1), f"Got out of bounds: {p}"
        self.pad.addch(*p, s)

    def plot_multiple(self, plots: list):
        """Takes a list of (x, y, char) tuples."""
        for plot in plots:
            self.plot((plot[0], plot[1]), plot[2])

    def write(self, point, s):
        p = self._to_pad_xy(point)
        assert (0 <= p[0] <= self.width - 1) and (0 <= p[1] <= self.height - 1), f"Got out of bounds: {p}"
        self.pad.addstr(*p, s)

    def wait_for_key(self):
        self.stdscr.getkey()

    def refresh(self):
        top_left_pad = (0, 0)
        top_left_window = (0, 0)
        bottom_right_window = (curses.LINES - 1, curses.COLS - 1)
        self.pad.refresh(*top_left_pad, *top_left_window, *bottom_right_window)

    def __enter__(self):
        self.stdscr = curses.initscr()
        self.pad = curses.newpad(self.height, self.width)
        self.stdscr.resize(self.height, self.width)  # Attempt at preventing final scroll-up
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.clear()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.write(self.b_min, "")  # Prevent exit message going through graphics
        self.refresh()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()


if __name__ == '__main__':
    with CursesVisualizer(((-10, -10), (10, 10))) as cv:
        cv.plot_multiple([(-10, -10, '\u2588'), (10, 10, '\u2588'), (-10, 10, '\u2588')])
        cv.plot((10, -10), '\u2588')
        cv.write((-5, 0), "Woop woop")
        cv.refresh()
        cv.wait_for_key()

