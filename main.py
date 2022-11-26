import pygame, random
from pygame.locals import *
from pygame import K_UP, K_RIGHT, K_DOWN, K_LEFT, KEYDOWN

UP = 'UP'
RIGHT = 'RIGHT'
DOWN = 'DOWN'
LEFT = 'LEFT'

def apple_random_respawn() -> tuple:
    x = random.randint(0,590)
    y = random.randint(20,590)
    return (x//10 * 10, y//10 * 10)

def snake_eat(snake_head_pos:tuple, apple_pos:tuple) -> bool:
    return (snake_head_pos[0] == apple_pos[0]) and (snake_head_pos[1] == apple_pos[1])

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da cobrinha')

snake = [(300, 300), (300, 310), (300, 320)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill('#FFFFFF')

apple = pygame.Surface((10, 10))
apple.fill('#FF0000')

apple_pos = apple_random_respawn()

my_direction = UP

def restart_game():
    global snake
    global my_direction
    global apple_pos
    global score
    global teste
    score = 0
    snake = [(300, 300), (300, 310), (300, 320)]
    my_direction = UP
    apple_pos = apple_random_respawn()

font = pygame.font.Font('freesansbold.ttf', 14)

score = 0

clock = pygame.time.Clock()


while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if event.type == KEYDOWN:
        if event.key == K_UP and my_direction is not DOWN:
            my_direction = UP
        if event.key == K_RIGHT and my_direction is not LEFT:
            my_direction = RIGHT
        if event.key == K_DOWN and my_direction is not UP:
            my_direction = DOWN
        if event.key == K_LEFT and my_direction is not RIGHT:
            my_direction = LEFT
        
    if snake_eat(snake[0], apple_pos):
        apple_pos = apple_random_respawn()
        snake.append((0, 0))
        score += 1

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            restart_game()

    # Check if snake collided with boundaries
    if snake[0][0] == 600 or snake[0][0] == -10 or snake[0][1] == 600 or snake[0][1] < 20:
        restart_game()


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    pygame.draw.line(screen, (40, 40, 40), (0, 20), (600,20))

    score_font = font.render(f'Score: {score}', True, '#FFFFFF')
    score_rect = score_font.get_rect(center=(300, 10))
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
