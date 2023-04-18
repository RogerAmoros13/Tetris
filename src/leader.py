import os
from settings import *
import pygame
import csv
import time

class Leader:
    def __init__(self, screen):
        self.open_file()
        self.max_pos = 5
        self.text = ""
        self.fix = "Inserte el nombre: "
        self.font = pygame.font.SysFont('hacknerdfontcompletemono', 20)
        self.img = self.font.render(self.fix + self.text, True, WHITE)
        self.rect = self.img.get_rect()
        self.rect.topleft = (430, 350)
        self.cursor = pygame.Rect(self.rect.topright, (3, self.rect.height))

        self.writting = False
        self.screen = screen

    def open_file(self, file=""):
        path = os.getcwd() + (file or "\\data\\ranking.csv")
        self.data = []
        with open(path, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                self.data.append(line)

    def write_file(self, file=""):
        path = os.getcwd() + (file or "\\data\\ranking.csv")
        with open(path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)

    def enter_ranking(self, result):
        for i, line in enumerate(self.data):
            if result > int(line[1]) and i < self.max_pos:
                return True
        return False

    def add_new_result(self, result):
        for iter, line in enumerate(self.data):
            if result > int(line[1]):
                break
        self.data.insert(iter, [self.text, result])
        self.data.pop()
    
    def draw_insert_name(self):
        if self.writting:
            self.img = self.font.render(self.fix + self.text, True, WHITE)
            self.rect.size = self.img.get_size()
            self.cursor.topleft = self.rect.topright
            self.screen.blit(self.img, self.rect)
            if time.time() % 1 > 0.5:
                pygame.draw.rect(self.screen, RED, self.cursor)
    
    def draw_ranking(self):
        inc = 0
        step = 60
        pygame.draw.line(self.screen, WHITE, (420, 500), (760, 500))
        for line in self.data:
            pygame.draw.line(self.screen, WHITE, (420, 500 + inc), (760, 500 + inc))
            img = self.font.render(line[0], True, WHITE)
            self.screen.blit(img, (430, 500 + inc + 10))
            img = self.font.render(str(line[1]) + " points", True, WHITE)
            self.screen.blit(img, (600, 500 + inc + 10))
            inc += step
