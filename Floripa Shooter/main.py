import pygame

pygame.init();
print("Pygame initialized")
window = pygame.display.set_mode(size=(600, 480))
print("Window created")

print("Entering main loop")
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close windows
            quit() #Exit program