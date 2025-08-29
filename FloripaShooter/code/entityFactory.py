#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Background import Background


class EntityFactory:
   @staticmethod
   def get_entity(entity_name: str):
       match entity_name:
           case 'Level1Bg':
                list_bg = []
                for i in range(8):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
           case 'player1':
                return Player('player1', (10, WIN_HEIGHT /2))
           
            
