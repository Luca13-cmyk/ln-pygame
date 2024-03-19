#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import IMAGE_LEVEL


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(IMAGE_LEVEL[entity_name]):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                return list_bg
