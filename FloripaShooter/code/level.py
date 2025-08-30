#!/usr/bin/python
# -*- coding: utf-8 -*-






import random
import sys
from pygame.font import Font
import pygame
from code.Enemy import Enemy
from code.Player import Player
from code.EntityMediator import EntityMediator
from code.Const import EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT, C_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory




class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # milliseconds
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('player1',))

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2',))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        
    def run(self ):
        pygame.mixer_music.load("./FloripaShooter/asset/music1.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(120)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if entity.name == 'player1':
                    self.level_text(text_size=20, text=f'Conceição - Vida: {entity.health}  -  Pontos: {entity.score}', text_color=(C_WHITE), text_pos=(10, 50))
                    #self.level_text(text_size=20, text=f'Score: {entity.score}', text_color=(C_WHITE), text_pos=(10, 60))
                if entity.name == 'player2':
                    self.level_text(text_size=20, text=f'Peri - Vida: {entity.health}  -  Pontos: {entity.score}', text_color=(C_WHITE), text_pos=(10, 65))
                    #self.level_text(text_size=20, text=f'Score: {entity.score}', text_color=(C_WHITE), text_pos=(10, 100))
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    
                
            self.level_text(text_size=30, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=(C_WHITE), text_pos=(10, 20))
            self.level_text(text_size=20, text=f'entidades: {len(self.entity_list)}', text_color=(C_WHITE), text_pos=(10, WIN_HEIGHT - 20))
            self.level_text(text_size=20, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=(10, WIN_HEIGHT - 34))
            
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True, italic=False)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)       

