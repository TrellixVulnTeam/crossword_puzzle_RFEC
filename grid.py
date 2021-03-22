from cell import Cell
from insertion_error import InsertionError
from wordslot import WordSlot
from typing import List


class Grid:

    def __init__(self, crossword: List[str]):
        """
        :param crossword: crossword[i][j] is empty if it is a valid position
        """
        self.grid = self.construct_puzzle(crossword)
        self.word_slots = self.get_word_slots(crossword)

    def get_word_slots(self, crossword: List[str]) -> List[WordSlot]:

        VERTICAL, HORIZONTAL = 1, 0
        seen_v, seen_h = set(), set()
        row_count, col_count = len(crossword), len(crossword[0])

        def dfs_horizontal(r: int, c: int) -> int:
            """
            :param r: Cell row
            :param c: Cell col
            :return: End index of end of word slot horizontally or None
            """
            def dfs(col: int) -> int:
                if col < col_count and crossword[r][col] == '-' and (r, col) not in seen_h:
                    seen_h.add((r, col))
                    return dfs(col + 1)
                else:
                    return col - 1
            return dfs(c)

        def dfs_vertical(r: int, c: int) -> int:
            """
            :param r: Cell row
            :param c: Cell column
            :return: End index of end of word slot vertically or None
            """
            def dfs(row: int) -> int:
                if row < row_count and crossword[row][c] == '-' and (row, c) not in seen_v:
                    seen_v.add((row, c))
                    return dfs(row + 1)
                else:
                    return row - 1
            return dfs(r)

        word_slots = []

        for i in range(row_count):
            for j in range(col_count):
                # get end index for horizontal word slot
                end_index_hori = dfs_horizontal(i, j)
                if end_index_hori > j:
                    length = end_index_hori - j + 1
                    cells = [self.get_cell(i, c) for c in range(j, end_index_hori + 1)]
                    word_slots.append(WordSlot(HORIZONTAL, length, i, j, cells))

                # get end index for vertical word slot
                end_index_vert = dfs_vertical(i, j)
                if end_index_vert > i:
                    length = end_index_vert - i + 1
                    cells = [self.get_cell(r, j) for r in range(i, end_index_vert + 1)]
                    word_slots.append(WordSlot(VERTICAL, length, i, j, cells))

        return word_slots

    @staticmethod
    def construct_puzzle(crossword) -> List[List[Cell]]:
        """
        :param crossword: crossword[i][j] is empty if it is a valid position
        :return: A 2x2 grid of cell objects
        """
        grid = []
        for i in range(len(crossword)):
            row = []
            for j in range(len(crossword[i])):
                val = crossword[i][j]
                row.append(Cell(i, j, val, val == "-"))
            grid.append(row)
        return grid

    def insert_words(self, words):
        """
        :param words: Insert words into the grid and return the new grid with words
        """
        def solve(to_insert) -> bool:
            if not to_insert:
                return True

            for slot in self.word_slots:
                try:
                    slot.insert(to_insert[0])
                    if solve(to_insert[1:]):
                        return True
                    slot.delete_word()

                except InsertionError:
                    continue
            return False

        if solve(words):
            return str(self)

    def get_cell(self, r, c) -> Cell:
        return self.grid[r][c]

    def __str__(self):
        string = ""

        for row_cells in self.grid:
            row = []

            for cell in row_cells:
                val = cell.get_val()
                if val.isalpha() or cell.is_open:
                    row.append(val)
                else:
                    row.append(".")
                row.append(" ")

            string += "".join(row)
            string += "\n"

        return string
