# Termial에 "pip install pygame"해서 설치 후 실행

import pygame
import sys

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Ball Game")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 공과 패들
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 20, 20)
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 30, 120, 20)
ball_speed = [5, 5]
paddle_speed = 10

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
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(paddle_speed, 0)

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽에 튕기기
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 공이 화면 아래로 떨어졌을 때
    if ball.bottom >= HEIGHT:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # 그리기
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, RED, paddle)

    pygame.display.flip()
    clock.tick(60)
