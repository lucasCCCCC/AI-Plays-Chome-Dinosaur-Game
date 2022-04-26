class Cactus:

    def __init__(self, img, cacti):
        self.img = img
        self.cacti = cacti
        self.rect = self.img[self.cacti].get_rect()
        self.rect.x = 900

    def draw(self, SCREEN):
        SCREEN.blit(self.img[self.cacti], self.rect)

    def update(self, speed, cactusList):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            cactusList.pop()


class SmallCactus(Cactus):
    def __init__(self, img, cacti):
        super().__init__(img, cacti)
        self.rect.y = 383


class LargeCactus(Cactus):
    def __init__(self, img, cacti):
        super().__init__(img, cacti)
        self.rect.y = 360
