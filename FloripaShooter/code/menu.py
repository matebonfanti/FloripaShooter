import pygame.image
import pygame.rect

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, C_GREEN, C_SELECT, C_WHITE, MENU_OPTION, WIN_HEIGHT, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./FloripaShooter/asset/menuBg.jpg")
        self.rect = self.surf.get_rect(left=0, top=0)
        

    def run(self):
        menu_option = 0
        pygame.mixer_music.load("./FloripaShooter/asset/Menu.mp3")
        pygame.mixer_music.play(-1)
        while True:
            # desenha o menu

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=120, text="Floripa", text_color=(C_GREEN), text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/10)))
            self.menu_text(text_size=80, text="Shooter", text_color=(C_GREEN), text_center_pos=((WIN_WIDTH/2), (WIN_HEIGHT/5)))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=(C_SELECT), text_center_pos=((WIN_WIDTH/2), 350 + 40*i))
                else:
                    self.menu_text(text_size=40, text=MENU_OPTION[i], text_color=(C_WHITE), text_center_pos=((WIN_WIDTH/2), 350 + 40*i))

            pygame.display.flip()
            


            #checa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                menu_option = (menu_option + 1) % len(MENU_OPTION)
                pygame.time.wait(150)
            if keys[pygame.K_UP]:
                menu_option = (menu_option - 1) % len(MENU_OPTION)
                pygame.time.wait(150)
            if keys[pygame.K_RETURN]:
                pygame.mixer_music.stop()
                return MENU_OPTION[menu_option]
                    

            
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size, bold=True, italic=False)
            text_surf: Surface = text_font.render (text, True, text_color).convert_alpha()
            text_Rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_Rect)
            
