#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Layer':
                list_bg = []
                for i in range(1, 7):
                    list_bg.append(Background(f'Layer{i}', position=(0, 0)))
                    list_bg.append(Background(f'Layer{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (120, WIN_HEIGHT / 2))
            case 'bat':
                return Enemy('bat', (WIN_WIDTH + 50, random.randint(50, WIN_HEIGHT - 100)))