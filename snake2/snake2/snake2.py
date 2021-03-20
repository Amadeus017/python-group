import pygame, sys, time, random
from pygame.constants import KEYDOWN
from pygame.math import Vector2

pygame.init()

snake_block = 20
cells = 25
dis_height = snake_block * cells
dis_width = snake_block * cells

display = pygame.display.set_mode((dis_height, dis_width))
pygame.display.set_caption('Snake Part 2')

apple = pygame.image.load('snake2/apple.png').convert_alpha()
blockimg = pygame.image.load('snake2/block.png').convert_alpha()
snkimg = pygame.image.load('snake2/head.png').convert_alpha()

class FOOD:
    def __init__(self):
        self.x = random.randint(0, cells - 1)
        self.y = random.randint(0, cells - 1)
        self.pos = Vector2(self.x, self.y)

    def food_draw(self):
        food_rect = pygame.Rect(self.pos.x * snake_block, self.pos.y * snake_block, snake_block, snake_block)
        display.blit(apple, food_rect)

    def randomiser(self):
        self.x = random.randint(0, cells - 1)
        self.y = random.randint(0, cells - 1)
        self.pos = Vector2(self.x, self.y)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(6, 10)]
        self.dir = Vector2(0, 0)
        self.grow = False

    def draw_snake(self):
        head_rect = pygame.Rect(self.body[0].x * snake_block, self.body[0].y * snake_block, snake_block, snake_block)
        display.blit(snkimg, head_rect)
        for block in self.body[1:]:
            snake_rect = pygame.Rect(block.x * snake_block, block.y * snake_block, snake_block, snake_block)
            display.blit(blockimg, snake_rect)

    def move(self):
        if self.grow == False:
            step = self.body[1:]
            step.insert(0, self.body[0] + self.dir)
            self.body = step[:]
        else:
            step = self.body[:]
            step.insert(0, self.body[0] + self.dir)
            self.body = step[:]
            self.grow = False

    def add(self):
        self.grow = True

    def reset(self):
        self.body = [Vector2(6, 10)]
        self.dir = Vector2(0, 0)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move()

    def draw(self):
        self.food.food_draw()
        self.snake.draw_snake()
        self.scoredraw()

    def eat(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomiser()
            self.snake.add()
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomiser()

    def scoredraw(self):
        text = 'Score: ' + str(len(self.snake.body) - 1)
        scoresurface = font.render(text, True, (56, 74, 112))
        score_x = int (snake_block * cells - 60)
        score_y = int (snake_block * cells - 40)
        score_rect = scoresurface.get_rect(center = (score_x, score_y))
        display.blit(scoresurface, score_rect)

    def gameover(self):
        self.snake.reset()

    def collide(self):
        if not 0 <= self.snake.body[0].x < cells or not 0 <= self.snake.body[0].y < cells:
            self.gameover()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()

game = MAIN()

SCREENUPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREENUPDATE, 150)

font = pygame.font.Font(None, 25)
clock = pygame.time.Clock();

snake = 10
speed = 60

surface = pygame.Surface((100, 200))

lightblue = (135, 206, 235)

close = False
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.dir = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                game.snake.dir = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                game.snake.dir = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                game.snake.dir = Vector2(1, 0)
        if event.type == SCREENUPDATE:
            game.snake.move()
    display.fill(lightblue)
    game.draw()
    game.eat()
    game.collide()
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
quit()