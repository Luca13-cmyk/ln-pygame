import pygame
from pygame import Surface

# Formatacao: CTRL + ALT + L

W_WIDTH = 576
W_HEIGHT = 324

# Inicializar o modulo pygame
pygame.init()
print("setup start")

# Criar janela pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superficie
bg_surf: Surface = pygame.image.load('./asset/bg.png')

# Desenhar na janela
window.blit(source=bg_surf, dest=(0, 0))

# Atualizar a janela
pygame.display.flip()
print("setup end")
clock = pygame.time.Clock()
running = True
print("loop start")
while running:
    # # poll for events
    # # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("loop end")
            running = False
    pass

    # # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")
    #
    # # RENDER YOUR GAME HERE
    #
    # # flip() the display to put your work on screen
    # pygame.display.flip()
    #
    # clock.tick(60)  # limits FPS to 60

pygame.quit()

# done
