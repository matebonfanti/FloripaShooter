import pygame


WIN_WIDTH  = 1024
WIN_HEIGHT = 559


MENU_OPTION = ('NEW GAME 1P', 
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - VERSUS',
               'SCORE',
                'EXIT')

COLOR_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)
C_SELECT = (255, 255, 50)

ENTITY_SPEED={
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level1Bg7': 7,
    'player1': 3,
    'player1Shoot': 5,
    'player2': 3,
    'player2Shoot': 5,
    'enemy1': 1,
    'enemy1Shoot': 2,
    'enemy2': 1,
    'enemy2Shoot': 6,
}

ENTITY_HEALTH={
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'player1': 3,
    'player1Shoot': 1,
    'player2': 3,
    'player2Shoot': 1,
    'enemy1': 50,
    'enemy1Shoot': 1,
    'enemy2': 60,
    'enemy2Shoot': 1,
}

ENTITY_DAMAGE={
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'player1': 1,
    'player1Shoot': 25,
    'player2':1,
    'player2Shoot': 20,
    'enemy1': 50,
    'enemy1Shoot': 20,
    'enemy2': 60,
    'enemy2Shoot': 25,
}

ENTITY_SHOOT_DELAY={
    'player1': 20,
    'player2': 10,
    'enemy1': 100,
    'enemy2': 80,
}



PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'player1': pygame.K_DOWN,
                   'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'player1': pygame.K_RIGHT,
                    'player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'player1': pygame.K_RCTRL,
                     'player2': pygame.K_LCTRL}


EVENT_ENEMY = pygame.USEREVENT + 1


SPAWN_TIME = 4000