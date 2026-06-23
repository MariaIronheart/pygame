#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_SIZE
from code.entity import Entity


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, PLAYER_SIZE)
        self.rect = self.surf.get_rect(center=position)

        self.attack_surf = pygame.image.load('./asset/attack.png').convert_alpha()
        self.attack_surf = pygame.transform.scale(self.attack_surf, (30, 30))
        self.attacking = False
        self.attack_x = -100
        self.attack_y = -100
        self.attack_speed = 12

    def update(self):
        pass

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_x = self.rect.right + 10
            self.attack_y = self.rect.centery

        if self.attacking:
            self.attack_x += self.attack_speed
            self.attack_rect = pygame.Rect(self.attack_x - 15, self.attack_y - 15, 30, 30)
            if self.attack_x > WIN_WIDTH:
                self.attacking = False
                self.attack_x = -100
                self.attack_y = -100
                self.attack_rect = pygame.Rect(-100, -100, 30, 30)