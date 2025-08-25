import pygame.image
import pygame.rect

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./FloripaShooter/asset/menuBg.jpg")
        self.rect = self.surf.get_rect(left=0, top=0)
        

    def run(self):
        pygame.mixer_music.load("./FloripaShooter/asset/Menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=120, text="Floripa", text_color=(255, 128, 0), text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/10)))
            self.menu_text(text_size=80, text="Shooter", text_color=(255, 155, 0), text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/5)))

            for i in range(len(MENU_OPTION)):
                 self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=(255, 255, 255), text_center_pos=((WIN_WIDTH/2), 350 + 40*i))


            
            pygame.display.flip()

            #checa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True, italic=False)
            text_surf: Surface = text_font.render (text, True, text_color).convert_alpha()
            text_Rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_Rect)
            
