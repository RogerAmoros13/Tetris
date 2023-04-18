from __future__ import annotations

from random import choice

import pygame
from figure import *
from grid import Grid
from numpy import log
from panel import Panel
from leader import Leader
from settings import *


class Tetris:
    def __init__(self, *args, **kwargs):
        # pygame configuration
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        self.grid = Grid()
        self.current_piece = None
        self.next_piece = self.get_available_pieces()
        self.points = 1000
        self.panel = Panel(self.screen)
        self.panel.next_piece = self.next_piece
        self.start = False
        self.leader = Leader(self.screen)

    def get_available_pieces(self):
        return choice(
            [
                FigureO(),
                FigureI(),
                FigureL(),
                FigureS(),
                FigureJ(),
                FigureT(),
                FigureZ(),
                # FigureOB(),
            ],
        )

    def spawn_next_piece(self):
        new_piece = self.get_available_pieces()
        self.current_piece = self.next_piece
        self.next_piece = new_piece
        if self.grid.add_figure(self.current_piece):
            return True
        return False

    def move_down(self):
        self.grid.move_down(self.current_piece)

    def move_right(self):
        self.grid.move_right(self.current_piece)

    def move_left(self):
        self.grid.move_left(self.current_piece)

    def rotate(self):
        self.grid.rotate(self.current_piece)

    def run(self):
        running = True
        move_clock = 0
        lose = False
        frames = 30
        pieces_spawned = 0
        pause = False
        while running:
            if not self.current_piece:
                if self.spawn_next_piece():
                    self.panel.next_piece = self.next_piece
                    pieces_spawned += 1
                else:
                    lose = True
                if pieces_spawned == 10:
                    frames -= 1
                    self.panel.level = 30 - frames
                    pieces_spawned = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if self.leader.writting:
                        if event.key == pygame.K_BACKSPACE:
                            if len(self.leader.text) > 0:
                                self.leader.text = self.leader.text[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.leader.writting = False
                            self.leader.add_new_result(self.points)
                            self.leader.write_file()
                            lose = False
                            self.restart()
                            frames = 30
                        else:
                            self.leader.text += event.unicode
                        continue
                    if lose:
                        continue
                    can_move = self.start and not pause
                    if event.key == pygame.K_DOWN and can_move:
                        self.move_down()
                    elif event.key == pygame.K_RIGHT and can_move:
                        self.move_right()
                    elif event.key == pygame.K_LEFT and can_move:
                        self.move_left()
                    elif event.key == pygame.K_UP and can_move:
                        self.rotate()
                    elif event.key == pygame.K_r:
                        self.restart()
                        frames = 30
                    elif event.key == pygame.K_p:
                        pause = not pause
                        self.panel.pause = pause
                    elif event.key == pygame.K_s:
                        self.start = True
            self.draw()
            if lose or pause or not self.start:
                if lose and not self.leader.writting:
                    if self.leader.enter_ranking(self.points):
                        self.leader.writting = True
                    else:
                        lose = False
                        self.restart()
                        frames = 30
                continue
            if move_clock == frames:
                self.move_down()
                move_clock = 0
            if self.current_piece and self.current_piece.blocked:
                self.current_piece = None
                lines = self.grid.check_lines()
                self.compute_points(lines)
            move_clock += 1
            self.clock.tick(30)

    def compute_points(self, inc):
        self.points += int(100 * inc * log(1 + inc))
        if self.points > 10000:
            self.points = 10000
        self.panel.points = self.points

    def draw(self):
        self.screen.fill(BLACK)
        self.grid.draw_grid(self.screen)
        self.panel.draw()
        self.leader.draw_ranking()
        if not self.start: 
            if self.leader.writting:
                self.draw_end_game()
            else:
                self.draw_start_log()
        
        self.leader.draw_insert_name()
        pygame.display.update()
    
    def draw_end_game(self):
        img = self.panel.font.render(
            "Partida finalizada!", True, WHITE,
        )
        self.screen.blit(img, (10, 220))
    
    def draw_start_log(self):
        img = self.panel.font.render(
            "Press s to start!", True, WHITE,
        )
        self.screen.blit(img, (10, 220))
    
    def restart(self):
        self.current_piece = None
        self.panel.points = 0
        self.panel.level = 1
        self.grid = Grid()
        self.points = 0
        self.start = False


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
