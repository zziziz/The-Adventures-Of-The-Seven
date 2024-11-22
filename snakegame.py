# Termial에 "pip install pygame"해서 설치 후 실행

import pygame
import random
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 뱀과 음식
block_size = 20
snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (block_size, 0)
food = (random.randrange(0, WIDTH, block_size), random.randrange(0, HEIGHT, block_size))

clock = pygame.time.Clock()

# 게임 루프
while True:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, block_size):
        snake_dir = (0, -block_size)
    if keys[pygame.K_DOWN] and snake_dir != (0, -block_size):
        snake_dir = (0, block_size)
    if keys[pygame.K_LEFT] and snake_dir != (block_size, 0):
        snake_dir = (-block_size, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-block_size, 0):
        snake_dir = (block_size, 0)

    # 뱀 이동
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # 음식 먹기
    if snake[0] == food:
        food = (random.randrange(0, WIDTH, block_size), random.randrange(0, HEIGHT, block_size))
    else:
        snake.pop()

    # 충돌 처리
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # 그리기
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, block_size, block_size))
    pygame.draw.rect(screen, RED, (*food, block_size, block_size))

    pygame.display.flip()
    clock.tick(10)
