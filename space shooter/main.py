import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True


surf =  pygame.Surface((100,100))
surf.fill("orange")

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill((255, 0, 0))
    # drow the game
    display_surface.blit(surf,(0,0))
    pygame.display.update()

pygame.quit()
