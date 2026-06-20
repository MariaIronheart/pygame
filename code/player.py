#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, PLAYER_SIZE
from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, PLAYER_SIZE)
        self.rect = self.surf.get_rect(center=position)

    def update(self, ):
        pass

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
