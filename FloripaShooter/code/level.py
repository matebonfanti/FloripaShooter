#!/usr/bin/python
# -*- coding: utf-8 -*-






import sys
from pygame.font import Font
import pygame
from code.Const import WIN_HEIGHT, C_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory




class Level:
    def __init__(self, window, name, game_mode):
        
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg', (0, 0)))
        self.timeout = 20000  # milliseconds
    def run(self ):
        pygame.mixer_music.load("./FloripaShooter/asset/music1.wav")
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(120)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=(C_WHITE), text_pos=((10), (WIN_HEIGHT - 20)))
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=C_WHITE, text_pos=((120, WIN_HEIGHT - 20)))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=(C_WHITE), text_pos=((160, WIN_HEIGHT - 20)))
            pygame.display.flip()
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True, italic=False)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)       

