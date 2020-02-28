import pygame

x = 500
y = 500

title = "Pong"

recketWidth = 100
racketHeight = 15

racketX = 200
racketY = 450

speed = 0

run = True

def racketBlock():
    global speedif racketX <= 0 or racketX >= x - racketWidth:
        speed = 0

def moveRacket():
    global racketX
    racketX += speed

pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption(title)

while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = -2
                if event.key == pygame.K_RIGHT:
                    speed = 2
    screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 40, 0), (racketX, racketY, recketWidth, racketHeight), 0)
        pygame.display.flip()
