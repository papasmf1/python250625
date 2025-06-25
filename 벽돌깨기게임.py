#설치
#pip install pygame
import pygame
import random

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
BRICK_COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, CYAN]

# 패들
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 40  # 크기를 2배 이상 크게 변경
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# 공
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [4, -4]

# 벽돌
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = []
brick_colors = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)
        color = BRICK_COLORS[row % len(BRICK_COLORS)]
        brick_colors.append(color)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽 충돌
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        # 게임 오버
        running = False

    # 패들 충돌
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 벽돌 충돌
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        brick_colors.pop(hit_index)
        ball_speed[1] = -ball_speed[1]

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for i, brick in enumerate(bricks):
        pygame.draw.rect(screen, brick_colors[i], brick)
    pygame.display.flip()

pygame.quit()