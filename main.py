import pygame

# Formatacao: CTRL + ALT + L
# Inicializar o modulo pygame
pygame.init()

# Criar janela
print("setup start")
window = pygame.display.set_mode(size=(600, 480))
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
