#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0, 0)):
        match entity_name:
            case 'Layer':
                list_bg = []
                for i in range(1, 7):
                    list_bg.append(Background(f'Layer{i}', position=(0, 0)))
                    list_bg.append(Background(f'Layer{i}', position=(WIN_WIDTH, 0)))
                return list_bg
        return None

