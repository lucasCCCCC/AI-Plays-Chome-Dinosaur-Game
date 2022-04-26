import pygame

DINOSAUR_RUN = [pygame.image.load("Game Assets/Dinosaur/DinosaurRun1.png"),
                pygame.image.load("Game Assets/Dinosaur/DinosaurRun2.png")]

DINOSAUR_JUMP = pygame.image.load("Game Assets/Dinosaur/DinosaurJump.png")


class Dinosaur:
    X = 70
    Y = 360
    speed_jump = 10

    def __init__(self, img=DINOSAUR_RUN[0]):
        self.img = img
        self.imgStep = 0
        self.JUMP = False
        self.jump_speed = self.speed_jump
        self.RUN = True
        self.rect = pygame.Rect(self.X, self.Y, img.get_width(), img.get_height())

    def updateDinosaur(self):
        if self.JUMP:
            self.jump()

        if self.RUN:
            self.run()

        if self.imgStep >= 40:
            self.imgStep = 0


    def draw(self, SCREEN):
        SCREEN.blit(self.img, (self.rect.x, self.rect.y))

    def jump(self):
        self.img = DINOSAUR_JUMP

        if self.JUMP:
            self.rect.y -= self.jump_speed * 3
            self.jump_speed -= 0.6

        if self.jump_speed <= -self.speed_jump:
            self.JUMP = False
            self.RUN = True
            self.jump_speed = self.speed_jump

    def run(self):
        self.img = DINOSAUR_RUN[self.imgStep // 20]
        self.rect.x = self.X
        self.rect.y = self.Y
        self.imgStep += 1
