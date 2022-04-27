import pygame
from random import randint
from dinosaur import Dinosaur
from cactus import SmallCactus, LargeCactus

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.SysFont("system", 40)

FLOOR = pygame.image.load("Game Assets/Floor/Floor.png")

LARGE_CACTI = [pygame.image.load("Game Assets/Cacti/LargeCacti21.png"),
               pygame.image.load("Game Assets/Cacti/LargeCacti22.png"),
               pygame.image.load("Game Assets/Cacti/LargeCacti23.png")]

SMALL_CACTI = [pygame.image.load("Game Assets/Cacti/SmallCacti11.png"),
               pygame.image.load("Game Assets/Cacti/SmallCacti12.png"),
               pygame.image.load("Game Assets/Cacti/SmallCacti13.png")]


def main():
    global score, speed, xFloor, yFloor, dinosaurs, cacti

    clock = pygame.time.Clock()
    dinosaurs = [Dinosaur()]

    score = 0
    speed = 10
    xFloor = 0
    yFloor = 443
    cacti = []

    def displayScore():
        global score, speed
        score += 1
        if score % 100 == 1:
            speed += 1

        s = FONT.render(str(score), True, "white")
        SCREEN.blit(s, [750, 25])

    def animateGround():
        global xFloor, yFloor
        SCREEN.blit(FLOOR, [xFloor, yFloor])
        SCREEN.blit(FLOOR, [FLOOR.get_width() + xFloor, yFloor])

        if xFloor <= -FLOOR.get_width():
            xFloor = 0
        xFloor -= speed

    def removeDinosaur(d):
        dinosaurs.pop(d)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((39, 41, 43))

        for dino in dinosaurs:
            dino.updateDinosaur()
            dino.draw(SCREEN)

        if len(dinosaurs) == 0:
            break

        if len(cacti) == 0:
            choice = randint(0, 1)

            if choice == 0:
                cacti.append(SmallCactus(SMALL_CACTI, randint(0, 2)))

            if choice == 1:
                cacti.append(LargeCactus(LARGE_CACTI, randint(0, 2)))

        for cacti_ in cacti:
            cacti_.draw(SCREEN)
            cacti_.update(speed, cacti)

            for x, dino in enumerate(dinosaurs):
                if dino.rect.colliderect(cacti_.rect):
                    removeDinosaur(x)

        keyPressed = pygame.key.get_pressed()

        for dino in dinosaurs:
            if keyPressed[pygame.K_UP] or keyPressed[pygame.K_SPACE]:
                dino.JUMP = True
                dino.RUN = False

        displayScore()
        animateGround()
        clock.tick(45)
        pygame.display.update()

    pygame.quit()
    quit()


main()
