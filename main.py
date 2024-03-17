import pygame
from pygame import Surface, Rect

# Formatacao: CTRL + ALT + L

W_WIDTH = 576
W_HEIGHT = 324

# Inicializar o modulo pygame
pygame.init()
print("setup start")

# Criar janela pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superficie
bg_surf: Surface = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surf: Surface = pygame.image.load('./asset/player1.png').convert_alpha()

# Obter o retangulo da superficie
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)

# Desenhar na janela (window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player1_surf, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()
print("setup end")

# Colocar um relogio no jogo
clock = pygame.time.Clock()
running = True

print("loop start")
while running:
    clock.tick(140)  # esse loop esta acontecendo 140 vezes por segundo
    # print(f'{clock.get_fps() :.0f}')  # executar o print do fps
    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player1_surf, dest=player1_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("loop end")
            running = False
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1

pygame.quit()
