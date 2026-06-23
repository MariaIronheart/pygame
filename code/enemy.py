#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import ENTITY_SPEED
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.passed = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def get_hitbox(self):
        return pygame.Rect(0, 0, 30, 30).move(
            self.rect.centerx - 15, self.rect.centery - 15
        )