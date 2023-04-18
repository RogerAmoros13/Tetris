from __future__ import annotations

import pygame
from settings import *


class Grid:
    def __init__(self, *args, **kwargs):
        self.rows = kwargs.get('rows', 20)
        self.cols = kwargs.get('cols', 10)
        self.grid = self._create_grid()

    def __str__(self):
        _str = ''
        _row = ''
        for i, cell in enumerate(reversed(self.grid)):
            _row = '{: <3}-({: <3},{: <3}, {}) | '.format(
                cell.position,
                cell.coord[0],
                cell.coord[1],
                '+' if cell.active else '-',
            ) + _row
            if i % 10 == 9:
                _str += '\n' + '-'*200 + '\n'
                _str += _row
                _row = ''
        return _str

    def _create_grid(self):
        grid = []
        for i in range(self.cols * self.rows):
            grid.append(Cell(i))
        return grid

    def draw_grid(self, screen):
        for cell in self.grid:
            cell.draw(screen)

    def add_figure(self, figure):
        cells = self.get_cells_by_id(figure.struct)
        success = True
        for cell in cells:
            if cell.active:
                success = False
            cell.color = figure.color
            cell.active = True
        return success

    def erase_figure(self, ids):
        cells = self.get_cells_by_id(ids)
        for cell in cells:
            cell.color = None
            cell.active = False

    def move_down(self, figure):
        self.erase_figure(figure.struct)
        figure.move_down(self)
        self.add_figure(figure)

    def move_right(self, figure):
        self.erase_figure(figure.struct)
        figure.move_right(self)
        self.add_figure(figure)

    def move_left(self, figure):
        self.erase_figure(figure.struct)
        figure.move_left(self)
        self.add_figure(figure)

    def rotate(self, figure):
        self.erase_figure(figure.struct)
        figure.rotate(self)
        self.add_figure(figure)

    def get_cells_by_id(self, ids):
        if isinstance(ids, int):
            for cell in self.grid:
                if cell.position == ids:
                    return cell
            return
        len_ids = len(ids)
        cells = []
        for cell_id in ids:
            for cell in self.grid:
                if cell.position == cell_id:
                    cells.append(cell)
                    break
            if len_ids == len(cells):
                break
        return cells

    def get_line(self, line):
        return self.grid[line * self.cols:(line + 1) * self.cols]

    def check_lines(self):
        lines_complete = 0
        for line in range(self.rows - 1, -1, -1):
            if self.is_complete_line(line):
                self.downgrade_lines(line)
                lines_complete += 1
        return lines_complete

    def downgrade_lines(self, line):
        for i in range(line, self.rows):
            upper_line = self.get_line(i + 1)
            lower_line = self.get_line(i)
            for up, low in zip(upper_line, lower_line):
                low.color, low.active = up.color, up.active

    def is_complete_line(self, line):
        for cell in self.get_line(line):
            if not cell.active:
                return False
        return True


class Cell:
    def __init__(self, position):
        self.position = position
        self.color = None
        self.coord = self._get_coord(position)
        self.little_coord = (
            self.coord[0] + 2,
            self.coord[1] + 2,
            self.coord[2] - 3,
            self.coord[3] - 3,
        )
        self.active = False

    def _get_coord(self, pos):
        x, y = (pos % 10) * 40, SIZE[0] - (pos // 10 + 1) * 40
        return x, y, 40, 40

    def draw(self, screen):
        pygame.draw.rect(
            surface=screen,
            color=GREY,
            rect=self.coord,
            width=1,
        )
        if self.color:
            pygame.draw.rect(
                surface=screen,
                color=self.color,
                rect=self.little_coord,
            )
