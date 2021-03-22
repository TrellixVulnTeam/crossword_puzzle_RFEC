class Cell:

    DEFAULT = "-"

    def __init__(self, r: int, c: int, val: str, is_open: bool):
        """
        :param r: Cell row
        :param c: Cell column
        :param is_open: True if it is open, False if not
        """

        self.r = r
        self.c = c
        self.val = val
        self.is_open = is_open
        self.use_count = 0

    def set_val(self, val):
        self.use_count += 1
        self.val = val
        self.is_open = False

    def reset(self):
        self.use_count -= 1
        if not self.use_count:
            self.val = Cell.DEFAULT
            self.is_open = True

    def get_val(self):
        return self.val

    def __repr__(self):
        return "Cell(val: {}, row: {}, col: {})".format(self.val, self.r, self.c)
