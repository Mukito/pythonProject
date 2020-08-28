import pygame

# inicializa o pygame
pygame.init()

# cria uma tela
screen = pygame.display.set_mode((800, 600))
#  Tiulo e Icone do jogo
pygame.display.set_caption('Espaço')
icon = pygame.image.load('icon3.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('space2.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

#Game loop
running = True
while running:

    # RGB - red, green, blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()

