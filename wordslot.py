from cell import Cell
from insertion_error import InsertionError
from typing import List


class WordSlot:
    ori = {1: "VERTICAL", 0: 'HORIZONTAL'}

    def __init__(self, orientation: int, length: int, r: int, c: int, cells: List[Cell]):
        self.orientation = orientation
        self.length = length
        self.r = r
        self.c = c
        self.cells = cells
        self.is_empty = True

    def get_word(self):
        return "".join([cell.val for cell in self.cells])

    def insert(self, word):
        if len(word) != self.length:
            raise InsertionError("Lengths do not match")

        if not self.is_empty:
            raise InsertionError("Slot is already filled")

        index = 0
        for letter, cell in zip(word, self.cells):
            if cell.is_open or cell.get_val() == letter:
                cell.set_val(letter)
                index += 1
            else:
                self.delete_word(index)
                raise InsertionError("WordSlot cannot be inserted")
        else:
            self.is_empty = False

    def delete_word(self, index=None):
        self.is_empty = True
        if index is None:
            index = self.length

        for i in range(index):
            self.cells[i].reset()
