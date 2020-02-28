import pygame

x = 500
y = 500

title = "Pong"

run = True

pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption(title)

while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.display.flip()