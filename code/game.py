#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW
from code.menu import Menu
from pygame.ftfont import Font


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def show_message(self, message, color):
        self.window.fill((0, 0, 0))
        font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=80)
        surf = font.render(message, True, color)
        rect = surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.window.blit(surf, rect)
        pygame.display.flip()
        pygame.time.wait(5000)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return == 'WIN':
                    self.show_message("YOU WON!", COLOR_WHITE)
                elif level_return == 'GAME_OVER':
                    self.show_message("GAME OVER", COLOR_WHITE)
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()