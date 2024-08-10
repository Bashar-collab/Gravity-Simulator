import pygame
from sys import exit
import math
import itertools
import random
import LCG

pygame.init()
Window_Size = (800, 600)
Window = pygame.display.set_mode(Window_Size)
Clock = pygame.time.Clock()

BackGround = pygame.Surface(Window_Size)
BackGround.fill("blue")
BackGround_Rect = BackGround.get_rect(center=(400, 300))

G = 6.67*10**-12
# G = 0.01
time_acc = 10**10
G *= time_acc
class Body(pygame.sprite.Sprite):
    def __init__(self, mass, radius, start_position, color, x_vel, y_vel):
        super().__init__()

        self.mass = mass
        self.radius = radius
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]

        self.x_vel = x_vel
        self.x_acc = 0
        self.y_vel = y_vel
        self.y_acc = 0

        self.color = color
        self.rect = pygame.Rect(
            self.x_pos - self.radius,
            self.y_pos - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def set_y_vel(self, value):
        self.y_vel = value

    def set_x_vel(self, value):
        self.x_vel = value

    def set_y_acc(self, value):
        self.y_acc = value

    def set_x_acc(self, value):
        self.x_acc = value

    def change_x_pos(self, value):
        self.x_pos += value

    def change_y_pos(self, value):
        self.y_pos += value

    def change_x_vel(self, value):
        self.x_vel += value

    def change_y_vel(self, value):
        self.y_vel += value

    def update_pos(self):
        self.rect.center = (round(self.x_pos), round(self.y_pos))

    def animate(self):
        self.change_x_vel(self.x_acc)
        self.change_y_vel(self.y_acc)

        if self.x_pos < self.radius:
            self.x_pos = self.radius
            self.x_vel = abs(self.x_vel)
        elif self.x_pos > Window_Size[0] - self.radius:
            self.x_pos = Window_Size[0] - self.radius
            self.x_vel = -abs(self.x_vel)
        if self.y_pos < self.radius:
            self.y_pos = self.radius
            self.y_vel = abs(self.y_vel)
        elif self.y_pos > Window_Size[1] - self.radius:
            self.y_pos = Window_Size[1] - self.radius
            self.y_vel = -abs(self.y_vel)

        self.change_x_pos(self.x_vel)
        self.change_y_pos(self.y_vel)

        self.update_pos()

    def gravitate(self, otherbody):
        dx = abs(self.x_pos - otherbody.x_pos)
        dy = abs(self.y_pos - otherbody.y_pos)

        if dx < self.radius * 2 and dy < self.radius * 2:
            pass
        else:
            try:
                r = math.sqrt(dx ** 2 + dy ** 2)
                a = G * otherbody.mass / r ** 2
                theta = math.asin(dy / r)

                if self.y_pos > otherbody.y_pos:
                    self.set_y_acc(-math.sin(theta) * a)
                else:
                    self.set_y_acc(math.sin(theta) * a)
                if self.x_pos > otherbody.x_pos:
                    self.set_x_acc(-math.cos(theta) * a)
                else:
                    self.set_x_acc(math.cos(theta) * a)
            except ZeroDivisionError:
                pass
            

body_group = pygame.sprite.Group()
BodyCount = 20


# body_group.add(
#         Body(
#             2*10**10,
#             30,
#             (400,300),
#             "black",
#             0,
#             0,
#         )
#     )

for i in range(BodyCount):
        body_group.add(
            Body(
                int(LCG.pseudo_uniform(1, 12, size = 100)[i]),
                int(LCG.pseudo_uniform(5, 15, size = 100)[i]),
                (random.randrange(100, 600), random.randrange(100, 600)),
                "white",
                0,
                0,
            )
        )

# LCG.plot(5,15)
body_list = list(body_group)
body_pairs = list(itertools.combinations(body_list, 2))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Window.blit(BackGround, BackGround_Rect)

    for body, otherbody in body_pairs:
        body.gravitate(otherbody)
        otherbody.gravitate(body)
        body.animate()
        otherbody.animate()

    for body in body_group:
        pygame.draw.circle(
            Window,
            body.color,
            (round(body.x_pos), round(body.y_pos)),
            body.radius,
        )

    pygame.display.update()
    Clock.tick(60)

