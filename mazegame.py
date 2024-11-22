# Termial에 "pip install pygame"해서 설치 후 실행

import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Escape")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 플레이어와 출구
player = pygame.Rect(50, 50, 30, 30)
goal = pygame.Rect(WIDTH - 80, HEIGHT - 80, 50, 50)
walls = [
    pygame.Rect(200, 100, 400, 20),
    pygame.Rect(200, 200, 20, 300),
    pygame.Rect(400, 300, 300, 20)
]

clock = pygame.time.Clock()

# 게임 루프
while True:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.move_ip(0, -5)
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.move_ip(0, 5)
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(5, 0)

    # 충돌 처리
    for wall in walls:
        if player.colliderect(wall):
            if keys[pygame.K_UP]:
                player.move_ip(0, 5)
            if keys[pygame.K_DOWN]:
                player.move_ip(0, -5)
            if keys[pygame.K_LEFT]:
                player.move_ip(5, 0)
            if keys[pygame.K_RIGHT]:
                player.move_ip(-5, 0)

    # 출구 도달
    if player.colliderect(goal):
        print("You Win!")
        pygame.quit()
        sys.exit()

    # 그리기
    pygame.draw.rect(screen, GREEN, goal)
    pygame.draw.rect(screen, BLACK, player)
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    pygame.display.flip()
    clock.tick(60)
