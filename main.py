import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

DINOSAUR_RUN = [pygame.image.load("Game Assets/Dinosaur/DinosaurRun1.png"),
                pygame.image.load("Game Assets/Dinosaur/DinosaurRun2.png")]

DINOSAUR_JUMP = pygame.image.load("Game Assets/Dinosaur/DinosaurJump.png")

FLOOR = pygame.image.load("Game Assets/Floor/Floor.png")

pygame.init()


def main():

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill((39, 41, 43))
        pygame.display.update()


    pygame.quit()
    quit()


main()
