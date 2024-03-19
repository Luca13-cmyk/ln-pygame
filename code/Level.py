#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.mode = menu_option  # opcao do menu
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
