# 뱀게임.py

import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)      # 사람 뱀
RED = (255, 0, 0)        # 먹이
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)     # AI 뱀

# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("사람 vs AI 뱀 게임")

clock = pygame.time.Clock()
font = pygame.font.SysFont("malgungothic", 30)

def draw_snake(snake, color):
    for pos in snake:
        pygame.draw.rect(screen, color, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_score(score, ai_score):
    score_text = font.render(f"사람: {score}   AI: {ai_score}", True, BLACK)
    screen.blit(score_text, [10, 10])

def ai_next_direction(ai_snake, food, ai_direction):
    head = ai_snake[0]
    # 단순한 그리디 알고리즘: 먹이와의 x, y 거리 우선
    dx = food[0] - head[0]
    dy = food[1] - head[1]
    # 우선 x축, 그 다음 y축
    if dx != 0 and ai_direction not in ['LEFT', 'RIGHT']:
        return 'RIGHT' if dx > 0 else 'LEFT'
    elif dy != 0 and ai_direction not in ['UP', 'DOWN']:
        return 'DOWN' if dy > 0 else 'UP'
    # 이미 같은 축에 있으면 방향 유지
    return ai_direction

def move_head(head, direction):
    if direction == 'UP':
        head[1] -= CELL_SIZE
    elif direction == 'DOWN':
        head[1] += CELL_SIZE
    elif direction == 'LEFT':
        head[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        head[0] += CELL_SIZE
    return head

def is_collision(head, snake, other_snake):
    # 벽 충돌
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # 자기 자신과 충돌
    if head in snake:
        return True
    # 상대 뱀과 충돌
    if head in other_snake:
        return True
    return False

def main():
    # 사람 뱀
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = 'RIGHT'
    change_to = direction

    # AI 뱀
    ai_snake = [[400, 300], [420, 300], [440, 300]]
    ai_direction = 'LEFT'

    # 먹이
    food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
    while food in snake or food in ai_snake:
        food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]

    score = 0
    ai_score = 0

    game_over = False
    winner = None

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to

        # 사람 뱀 이동
        head = snake[0][:]
        head = move_head(head, direction)

        # AI 뱀 이동
        ai_direction = ai_next_direction(ai_snake, food, ai_direction)
        ai_head = ai_snake[0][:]
        ai_head = move_head(ai_head, ai_direction)

        # 충돌 체크
        if is_collision(head, snake, ai_snake):
            game_over = True
            winner = "AI"
        elif is_collision(ai_head, ai_snake, snake):
            game_over = True
            winner = "사람"
        elif head == ai_head:
            game_over = True
            winner = "무승부"

        # 이동 적용
        snake.insert(0, head)
        ai_snake.insert(0, ai_head)

        # 먹이 먹음
        if head == food and ai_head == food:
            score += 1
            ai_score += 1
            # 새 먹이
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
            while food in snake or food in ai_snake:
                food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        elif head == food:
            score += 1
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
            while food in snake or food in ai_snake:
                food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            snake.pop()

        if ai_head == food and head != food:
            ai_score += 1
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
            while food in snake or food in ai_snake:
                food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            ai_snake.pop()

        screen.fill(WHITE)
        draw_snake(snake, GREEN)
        draw_snake(ai_snake, BLUE)
        draw_food(food)
        show_score(score, ai_score)
        pygame.display.update()
        clock.tick(10)

    # 게임 오버 메시지
    screen.fill(WHITE)
    if winner == "무승부":
        msg = font.render("무승부!", True, RED)
    else:
        msg = font.render(f"{winner} 승리!", True, RED)
    screen.blit(msg, [WIDTH // 2 - 70, HEIGHT // 2 - 20])
    show_score(score, ai_score)
    pygame.display.update()
    pygame.time.wait(2500)

if __name__ == "__main__":
    main()