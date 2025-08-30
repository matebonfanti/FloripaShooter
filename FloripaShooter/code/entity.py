#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/level1/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 50000
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'
    @abstractmethod
    def move(self, ):
        
        pass
