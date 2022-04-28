import neat
import pygame
import os
import math
from random import randint
from dinosaur import Dinosaur
from cactus import SmallCactus, LargeCactus

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.SysFont("system", 40)
FONT2 = pygame.font.SysFont("system", 20)


FLOOR = pygame.image.load("Game Assets/Floor/Floor.png")

LARGE_CACTI = [pygame.image.load("Game Assets/Cacti/LargeCacti21.png"),
               pygame.image.load("Game Assets/Cacti/LargeCacti22.png"),
               pygame.image.load("Game Assets/Cacti/LargeCacti23.png")]

SMALL_CACTI = [pygame.image.load("Game Assets/Cacti/SmallCacti11.png"),
               pygame.image.load("Game Assets/Cacti/SmallCacti12.png"),
               pygame.image.load("Game Assets/Cacti/SmallCacti13.png")]


def eval_genomes(genomes, config):

    global score, speed, xFloor, yFloor, dinosaurs, cacti, ge, nets

    clock = pygame.time.Clock()

    score = 0
    speed = 10
    xFloor = 0
    yFloor = 443
    cacti = []

    dinosaurs = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        dinosaurs.append(Dinosaur())
        ge.append(genome)


    def computeDistance(d, c):
        return math.sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2)


    def displayScore():
        global score, speed
        score += 1
        if score % 100 == 1:
            speed += 0.5

        s = FONT.render(str(score), True, "white")
        SCREEN.blit(s, [750, 25])


    def displayGeneration():
        g = FONT2.render("Generation: " + str(population.generation + 1), True, "white")
        p = FONT2.render("Population: " + str(len(dinosaurs)), True, "white")

        SCREEN.blit(g, [25, 25])
        SCREEN.blit(p, [25, 50])


    def animateGround():
        global xFloor, yFloor
        SCREEN.blit(FLOOR, [xFloor, yFloor])
        SCREEN.blit(FLOOR, [FLOOR.get_width() + xFloor, yFloor])

        if xFloor <= -FLOOR.get_width():
            xFloor = 0
        xFloor -= speed


    def removeDinosaur(d):
        dinosaurs.pop(d)
        nets.pop(d)
        ge.pop(d)


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

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
                    ge[x].fitness -= 0.5
                    removeDinosaur(x)

        # keyPressed = pygame.key.get_pressed()

        # for dino in dinosaurs:
            # if keyPressed[pygame.K_UP] or keyPressed[pygame.K_SPACE]:
                # dino.JUMP = True
                # dino.RUN = False

        for x, dino in enumerate(dinosaurs):
            nnOutput = nets[x].activate((dino.rect.y, computeDistance((dino.rect.x, dino.rect.y),
                                                                      cacti_.rect.midtop)))

            if nnOutput[0] > 0.5 and dino.rect.y == dino.Y:
                dino.JUMP = True
                dino.RUN = False


        displayScore()
        animateGround()
        displayGeneration()

        clock.tick(45)
        pygame.display.update()


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    global population

    population = neat.Population(config)
    population.run(eval_genomes, 100)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)
