import pygame
from dinosaur import Dinosaur

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.SysFont("system", 40)


FLOOR = pygame.image.load("Game Assets/Floor/Floor.png")

def main():

    clock = pygame.time.Clock()
    dinosaurs = [Dinosaur()]

    global score, speed, xFloor, yFloor
    score = 0
    speed = 10
    xFloor = 0
    yFloor = 443

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


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((39, 41, 43))

        for dino in dinosaurs:
            dino.updateDinosaur()
            dino.draw(SCREEN)


        keyPressed = pygame.key.get_pressed()

        for x, dino in enumerate(dinosaurs):
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
