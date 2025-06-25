import pygame
import sys
import random

# --- 상수 정의 ---
# 화면 크기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 뱀의 이동 방향
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 게임 속도
FPS = 10

# --- 핵심 게임 로직을 담은 클래스 ---
class SnakeGame:
    def __init__(self):
        """게임 초기화"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Python Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('malgungothic', 30) # 시스템에 따라 폰트 변경 (e.g., 'arial')
        self.reset_game()

    def reset_game(self):
        """게임을 초기 상태로 리셋"""
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        """먹이를 랜덤 위치에 생성"""
        while True:
            food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            # 먹이가 뱀의 몸통과 겹치지 않도록 함
            if food_pos not in self.snake:
                return food_pos

    def handle_events(self):
        """사용자 입력 처리"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def move_snake(self):
        """뱀을 이동시키고 충돌을 확인"""
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # 벽 충돌 확인
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_over = True
            return

        # 자기 자신과 충돌 확인
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 먹이 먹었는지 확인
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw_elements(self):
        """화면에 게임 요소들을 그림"""
        self.screen.fill(BLACK)
        
        # 뱀 그리기
        for segment in self.snake:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect)

        # 먹이 그리기
        food_rect = pygame.Rect(self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)

        # 점수 표시
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        pygame.display.flip() # 화면 업데이트

    def show_game_over_screen(self):
        """게임 오버 화면 표시"""
        self.screen.fill(BLACK)
        game_over_font = pygame.font.SysFont('malgungothic', 50)
        score_font = pygame.font.SysFont('malgungothic', 30)

        game_over_text = game_over_font.render("GAME OVER", True, RED)
        score_text = score_font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = score_font.render("Press any key to restart", True, WHITE)
        
        # 텍스트 중앙 정렬
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
        pygame.display.flip()

        # 키 입력을 기다림
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def run(self):
        """메인 게임 루프"""
        while True: # 게임 재시작을 위한 외부 루프
            self.reset_game()
            
            while not self.game_over: # 한 판의 게임 루프
                self.handle_events()
                self.move_snake()
                self.draw_elements()
                self.clock.tick(FPS)
            
            # 게임 오버 화면
            self.show_game_over_screen()


# --- 게임 실행 ---
if __name__ == '__main__':
    game = SnakeGame()
    game.run()