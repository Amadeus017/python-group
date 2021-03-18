import pygame, sys, pymunk, time, random
from pygame.constants import KEYDOWN, K_LEFT, K_UP
from pygame.math import Vector2

positive_y_is_up = True

class BALL:
    def __init__(self, space):
        self.body = pymunk.Body(1, 10, body_type=pymunk.Body.DYNAMIC)
        self.space = space

    def makeball(self):
        self.body.position = ((window_width // 3), 20)
        shape = pymunk.Circle(self.body, 60)
        shape.elasticity = 0.9
        self.space.add(self.body, shape)

    def draw(self):
        ball_rect = pygame.Rect(self.body.position.x - 60, self.body.position.y - 60, 120, 120)
        screen.blit(ballimg, ball_rect)


class CAR:
    def __init__(self, space):
        self.body = pymunk.Body(100, 10, body_type=pymunk.Body.DYNAMIC)
        self.space = space

    def makecar(self):
        self.body.position = ((window_width // 3), 500)
        shape = pymunk.Circle(self.body, 30)
        shape.elasticity = 0.69
        self.space.add(self.body, shape)

    def move(self, v):
        self.body.position += v

    def draw(self):
        ball_rect = pygame.Rect(self.body.position.x -
                                60, self.body.position.y - 40, 120, 120)
        screen.blit(carimg, ball_rect)

class WALLANDGOAL:
    def __init__(self, space):
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.space = space

    def makewalls(self):
        wall1 = pymunk.Segment(self.body, [0, window_length + 500], [window_width, window_length + 500], 500)
        wall2 = pymunk.Segment(self.body, [window_width, -500], [0, -500], 500)
        wall3 = pymunk.Segment(self.body, [0, 0], [0, window_length], 10)
        wall4 = pymunk.Segment(self.body, [window_width, 0], [window_width, window_length], 10)
        wall1.elasticity = wall2.elasticity = wall3.elasticity = wall4.elasticity = 0.99
        goal = pymunk.Segment(self.body, [window_width - 300, window_length - 360], [window_width, window_length - 360], 20)
        goal.elasticity = 0.69
        self.space.add(self.body, goal, wall1, wall2, wall3, wall4)

    def draw(self):
        pygame.draw.line(screen, pygame.Color('green'), [0, window_length], [window_width, window_length], 10)
        pygame.draw.line(screen, pygame.Color('red'), [window_width - 300, window_length - 360], [window_width, window_length - 360], 20)

pygame.init()
window_width, window_length = 1800, 800
screen = pygame.display.set_mode((window_width, window_length))
ballimg = pygame.image.load('2DRL/ball.png').convert_alpha()
carimg = pygame.image.load('2DRL/car.png').convert_alpha()
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 25)
space = pymunk.Space()
space.gravity = (0, 300)
ball = BALL(space)
ball.makeball()
car = CAR(space)
car.makecar()
walls = WALLANDGOAL(space)
walls.makewalls()
key = {pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
        pygame.K_UP: (0, 1), pygame.K_DOWN: (0, -1)}


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key in key:
                v = Vector2(key[event.key]) * 20
                car.move(v)
    screen.fill(pygame.Color('grey'))
    ball.draw()
    walls.draw()
    car.draw()
    space.step(1/50)
    pygame.display.update()
    clock.tick(60)
