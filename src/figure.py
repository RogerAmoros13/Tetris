from __future__ import annotations

from random import choice

from settings import *


class BasicFigure:
    def __init__(self):
        self.color = choice(
            [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE],
        )
        self.blocked = False

    def move_down(self, grid):
        new_struct = (
            self.struct[0] - 10,
            self.struct[1] - 10,
            self.struct[2] - 10,
            self.struct[3] - 10,
        )
        if self.check_available_struct(new_struct, grid):
            self.struct = new_struct

    def move_right(self, grid):
        new_struct = (
            self.struct[0] + 1,
            self.struct[1] + 1,
            self.struct[2] + 1,
            self.struct[3] + 1,
        )
        if self.check_available_struct(new_struct, grid, right=True):
            self.struct = new_struct

    def move_left(self, grid):
        new_struct = (
            self.struct[0] - 1,
            self.struct[1] - 1,
            self.struct[2] - 1,
            self.struct[3] - 1,
        )
        if self.check_available_struct(new_struct, grid, left=True):
            self.struct = new_struct

    def rotate(self, grid):
        pass

    def check_available_struct(self, struct, grid, left=False, right=False):
        for pos in struct:
            if not self.check_available_square(pos, grid, left, right):
                return False
        return True

    def check_available_square(self, pos, grid, left=False, right=False):
        if pos < 0:
            self.blocked = True
            return False
        if left and pos % 10 == 9:
            return False
        if right and pos % 10 == 0:
            return False
        if grid.get_cells_by_id(pos).active:
            if not (left or right):
                self.blocked = True
            return False
        return True


class FigureO(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (194, 195, 184, 185)
        self.name = 'figureo'

    def __str__(self):
        return 'Figure O'


class FigureOB(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (194, 195, 196, 184, 185, 186, 174, 175, 176)

    def __str__(self):
        return 'Figure O'


class FigureI(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (195, 185, 175, 165)
        self.vertical = True
        self.name = 'figurei'

    def __str__(self):
        return 'Figure I'

    def rotate(self, grid):
        if self.vertical:
            inc = (-11, 0, 11, 22)
        else:
            inc = (11, 0, -11, -22)
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.vertical = not self.vertical


class FigureL(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (195, 185, 175, 176)
        self.align = 'right'
        self.name = 'figurel'

    def __str__(self):
        return 'Figure L'

    def rotate(self, grid):
        if self.align == 'right':
            inc = (-9, 0, 9, -2)
            new_align = 'down'
        elif self.align == 'down':
            inc = (-11, 0, 11, 20)
            new_align = 'left'
        elif self.align == 'left':
            inc = (9, 0, -9, 2)
            new_align = 'up'
        else:
            inc = (11, 0, -11, -20)
            new_align = 'right'
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.align = new_align


class FigureS(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (183, 184, 194, 195)
        self.vertical = True
        self.name = 'figures'

    def __str__(self):
        return 'Figure S'

    def rotate(self, grid):
        if self.vertical:
            inc = (11, 0, -9, -20)
        else:
            inc = (-11, 0, 9, 20)
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.vertical = not self.vertical


class FigureJ(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (195, 185, 175, 174)
        self.align = 'left'
        self.name = 'figurej'

    def __str__(self):
        return 'Figure J'

    def rotate(self, grid):
        if self.align == 'right':
            inc = (9, 0, -9, -20)
            new_align = 'down'
        elif self.align == 'down':
            inc = (11, 0, -11, -2)
            new_align = 'left'
        elif self.align == 'left':
            inc = (-9, 0, 9, 20)
            new_align = 'up'
        else:
            inc = (-11, 0, 11, 2)
            new_align = 'right'
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.align = new_align


class FigureT(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (194, 195, 196, 185)
        self.align = 'up'
        self.name = 'figuret'

    def __str__(self):
        return 'Figure T'

    def rotate(self, grid):
        if self.align == 'right':
            inc = (-20, -11, -2, 0)
            new_align = 'down'
        elif self.align == 'down':
            inc = (-2, 9, 20, 0)
            new_align = 'left'
        elif self.align == 'left':
            inc = (20, 11, 2, 0)
            new_align = 'up'
        else:
            inc = (2, -9, -20, 0)
            new_align = 'right'
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.align = new_align


class FigureZ(BasicFigure):
    def __init__(self):
        super().__init__()
        self.struct = (193, 194, 184, 185)
        self.vertical = False
        self.name = 'figurez'

    def __str__(self):
        return 'Figure Z'

    def rotate(self, grid):
        if self.vertical:
            inc = (-2, 9, 0, 11)
        else:
            inc = (2, -9, 0, -11)
        new_struct = (
            self.struct[0] + inc[0],
            self.struct[1] + inc[1],
            self.struct[2] + inc[2],
            self.struct[3] + inc[3],
        )
        if self.check_available_struct(new_struct, grid, True, True):
            self.struct = new_struct
            self.vertical = not self.vertical
