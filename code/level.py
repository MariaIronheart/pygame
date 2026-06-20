#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Layer'))
        self.entity_list.append(EntityFactory.get_entity('Player'))

        self.spawn_timer = 0
        self.spawn_interval = 90  # frames entre cada novo morcego

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = 0
                self.entity_list.append(EntityFactory.get_entity('bat'))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            clock.tick(60)