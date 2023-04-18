from __future__ import annotations

import pygame
from settings import *


class Panel:
    def __init__(self, screen):
        self.next_piece = None
        self.screen = screen
        self.struct = []
        self.pause = False
        self.level = 1
        self.points = 0
        pygame.font.init()
        self.font = pygame.font.SysFont('hacknerdfontcompletemono', 40)

    def draw(self):
        self.draw_level()
        self.draw_next_piece()
        self.draw_points()
        self.draw_pause()
    
    def draw_pause(self):
        if self.pause:
            img = self.font.render(
                "P", True, WHITE,
            )
            self.screen.blit(img, (760, 760))

    def draw_points(self):
        img = self.font.render(
            f'Score: {str(self.points).zfill(5)}', True, WHITE,
        )
        self.screen.blit(img, (440, 400))

    def draw_level(self):
        img = self.font.render(
            f'Level: {self.level}', True, WHITE,
        )
        self.screen.blit(img, (480, 300))

    def draw_next_piece(self):
        draw_function = getattr(
            self,
            f'draw_{self.next_piece.name}',
        )
        draw_function()

    def draw_figureo(self):
        struct = [(550, 100), (590, 100), (550, 140), (590, 140)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figurei(self):
        struct = [(580, 80), (580, 120), (580, 160), (580, 200)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figurel(self):
        struct = [(580, 100), (580, 140), (580, 180), (620, 180)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figurez(self):
        struct = [(540, 100), (580, 100), (580, 140), (620, 140)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figures(self):
        struct = [(580, 100), (620, 100), (540, 140), (580, 140)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figurej(self):
        struct = [(580, 80), (580, 120), (580, 160), (580, 200)]
        struct = [(580, 100), (580, 140), (580, 180), (540, 180)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_figuret(self):
        struct = [(540, 100), (580, 100), (620, 100), (580, 140)]
        for elem in struct:
            self.draw_square(elem[0], elem[1])

    def draw_square(self, x, y):
        coord = x, y, 40, 40
        little_coord = x + 2, y + 2, 37, 37
        pygame.draw.rect(
            surface=self.screen,
            color=GREY,
            rect=coord,
            width=1,
        )
        pygame.draw.rect(
            surface=self.screen,
            color=self.next_piece.color,
            rect=little_coord,
        )
