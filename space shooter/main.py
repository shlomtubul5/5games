import pygame as pg

# general setup
pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

# plain surf
x = 0
surf = pg.Surface((100, 100))
surf.fill("orange")

# importing an image
player_surf = pg.image.load("images/player.png")


while running:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    display_surface.fill((255, 0, 0))
    # drow the game
    x += 0.1
    display_surface.blit(surf, (x, 0))
    pg.display.update()

pg.quit()
